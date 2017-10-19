# coding=utf-8
from django.shortcuts import render,redirect
from users.login_validate import user_login
from shoppingCart.models import Carinfo
from users.models import Userinfo
from .models import *
from datetime import datetime
from random import randint
from django.db import transaction
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST

# Create your views here.

@require_POST
@user_login
def order(request):
    cid_list = request.POST.get('cid','')
    if cid_list == '':
        return redirect('shopping:cart')
    uid = request.session['user_id']
    cid_list1 = cid_list.split('-')[:-1]
    cids = [int(x) for x in cid_list1]
    carts = Carinfo.objects.filter(id__in=cids)
    if carts[0].user_id != uid:
        return redirect('/')
    user = Userinfo.objects.get(id=uid)
    address = user.addressinfo_set.all()
    content = {'page_num':1,'title':'订单','carts':carts,'address':address,'cids':cid_list}
    return render(request,'order/place_order.html',content)


'''
transaction.atomic():开启事务，内部块用with语句包裹，当视图任何部分出现异常时，内部块中的操作被回滚
handler需要处理的操作有：
1、存储订单信息
2、删除购物车对应内容
3、修改商品库存
'''
@transaction.atomic
@require_POST
def order_handler(request):
    post = request.POST
    cid_list = post['cid']
    cid_list1 = cid_list.split('-')[:-1]
    cids = [int(x) for x in cid_list1]
    address = post['address']
    total = float(post['total'])
    pay_state = int(post['order_state'])
    now = datetime.now()
    uid = request.session['user_id']
    # 使用事务
    with transaction.atomic():
        # 生成订单
        order = Orderinfo()
        order_id = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
        order.oid = order_id
        order.oaddress = address
        order.odate = now
        order.ototal = total
        order.opay_id = pay_state
        order.ouser_id = uid
        num = randint(1,4)
        order.ostate_id = num
        order.save()
        carts = Carinfo.objects.filter(id__in=cids)
        # 库存删减、生成订单详情和购物车信息更新
        for cart in carts:
            goods = cart.goods
            goods.grepertory -=cart.counts
            goods.save()
            # 生成订单详情
            detail = Orderdetail()
            detail.oprice = goods.gprice
            detail.ocount = cart.counts
            detail.dorder_id = order_id
            detail.ogoods_id = goods.id
            detail.save()
            # 删除购物车对应信息
            cart.delete()
    return redirect('/users/center_order/1')
