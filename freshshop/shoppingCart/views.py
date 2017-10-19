# coding=utf-8
from django.shortcuts import render
from .models import Carinfo
from users.login_validate import user_login
from django.http import JsonResponse
from django.views.decorators.http import require_GET,require_POST
# Create your views here.

@require_GET
@user_login
def cart(request):
    carts = Carinfo.objects.filter(user_id=request.session['user_id'])
    content = {'page_num':1,'title':'购物车','carts':carts}
    return render(request,'shoppingCart/cart.html',content)


@require_GET
@user_login
def add_cart(request,gid,count):
    gid = int(gid)
    count = int(count)
    uid = request.session['user_id']
    cart = Carinfo.objects.filter(user_id=uid,goods_id=gid)
    if len(cart)>=1:
        cart[0].counts +=count
        cart[0].save()
    else:
        cart_new = Carinfo()
        cart_new.user_id = uid
        cart_new.goods_id = gid
        cart_new.counts = count
        cart_new.save()
    count_all = Carinfo.objects.filter(user_id=uid).count()
    return JsonResponse({'counts':count_all})


@require_GET
def cart_nums(request):
    try:
        uid = request.session.get('user_id','')
        nums = Carinfo.objects.filter(user_id=uid).count()
        status = nums
    except Exception as e:
        status = 0
    return JsonResponse({'status':status})


@require_POST
def cart_edit(request,cid,count):
    try:
        cid = int(cid)
        count = int(count)
        cart = Carinfo.objects.get(id=cid)
        cart.counts =count
        cart.save()
    except Exception as e:
        count = Carinfo.objects.get(id=cid).counts
    return JsonResponse({'count':count})


@require_POST
def del_cart(request,cid):
    cart = Carinfo.objects.get(id=int(cid))
    try:
        cart.delete()
        status = 0
    except Exception as e:
        status = 1
    return JsonResponse({'status':status})