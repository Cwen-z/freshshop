# coding=utf-8
from django.shortcuts import render
from .models import *
from shoppingCart.models import Carinfo
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from haystack.views import SearchView
# Create your views here.

@require_GET
def index(request):
    # 选择所有分类，按照分类选出新添加的4个数据和点击量最高的3个数据
    # 分别作为index页面的分类展示和分类商品展示
    type = Typeinfo.objects.all()
    type0 = type[0].goodsinfo_set.order_by('-id')[:4]# 第一个分类中最新添加的4个
    type01 = type[0].goodsinfo_set.order_by('-gclick')[:3] # 点击量最高的3个
    type1 = type[1].goodsinfo_set.order_by('-id')[:4]
    type11 = type[1].goodsinfo_set.order_by('-gclick')[:3]
    type2 = type[2].goodsinfo_set.order_by('-id')[:4]
    type21 = type[2].goodsinfo_set.order_by('-gclick')[:3]
    type3 = type[3].goodsinfo_set.order_by('-id')[:4]
    type31 = type[3].goodsinfo_set.order_by('-gclick')[:3]
    type4 = type[4].goodsinfo_set.order_by('-id')[:4]
    type41 = type[4].goodsinfo_set.order_by('-gclick')[:3]
    type5 = type[5].goodsinfo_set.order_by('-id')[:4]
    type51 = type[5].goodsinfo_set.order_by('-gclick')[:3]
    uid = request.session.get('user_id', '')
    nums = 0
    if uid != '':
        nums = Carinfo.objects.filter(user_id=uid).count()
    content = {'page_num':2,'title':'首页',
               'nums':nums,'type':type,
               'type0':type0,'type01':type01,
               'type1':type1,'type11':type11,
               'type2':type2,'type21':type21,
               'type3':type3,'type31':type31,
               'type4':type4,'type41':type41,
               'type5':type5,'type51':type51}
    response = render(request,'goods/index.html',content)
    response.set_cookie('url', request.get_full_path())
    return response


@require_GET
def detail(request,p1):
    type = Typeinfo.objects.all()
    goods = Goodsinfo.objects.get(id=int(p1))
    goods.gclick +=1
    goods.save()
    title1 = goods.gtype.title
    news = goods.gtype.goodsinfo_set.order_by('-id')[:2]
    repertory = goods.grepertory
    uid = request.session.get('user_id', '')
    nums = 0
    if uid != '':
        nums = Carinfo.objects.filter(user_id=uid).count()
    content = {'page_num':2,'title':'商品详情','nums':nums,'title1':title1,'goods':goods,'news':news,'type':type,'repertory':repertory}
    response = render(request,'goods/detail.html',content)
    goods_ids = request.COOKIES.get('goods_ids', '')
    if goods_ids != '':
        goods_ids_list = goods_ids.split(',')
        if p1 in goods_ids_list:
            goods_ids_list.remove(p1)
        goods_ids_list.insert(0,p1)
        if len(goods_ids_list) >= 6:
            del goods_ids_list[5]
        goods_id = ",".join(goods_ids_list)
    else:
        goods_id = p1
    response.set_cookie('goods_ids', goods_id)
    response.set_cookie('url', request.get_full_path())
    return response

@require_GET
def good_list(request,tid,sort,pn):
    types = Typeinfo.objects.all()
    type = Typeinfo.objects.get(id=tid)
    news = type.goodsinfo_set.order_by('-id')[:2]
    if sort == '1': # 默认排序
        goods = type.goodsinfo_set.all()
    if sort == '2': # 价格排序
        goods = type.goodsinfo_set.order_by('gprice')
    if sort == '3':  # 人气排序
        goods = type.goodsinfo_set.order_by('-gclick')
    paginator = Paginator(goods, 9)
    page = paginator.page(int(pn))
    uid = request.session.get('user_id', '')
    nums = 0
    if uid != '':
        nums = Carinfo.objects.filter(user_id=uid).count()
    content = {'page_num':2,'title':'商品列表','nums':nums,'type1':type,'page':page,'paginator':paginator,
               'news':news,'type':types,'sort':int(sort)}
    response = render(request, 'goods/list.html', content)
    response.set_cookie('url', request.get_full_path())
    return response

# 获取当前用户的购物车数量
def cart_count(request):
    if request.session.has_key('user_id'):
        return Carinfo.objects.filter(user_id=request.session['user_id']).count()
    else:
        return 0

def type_list(request):
    if request.session.has_key('user_id'):
        return Typeinfo.objects.all()
    else:
        return ''

# 自定义搜索页面的上下文
class MySearch(SearchView):
    def extra_context(self):
        context = super(MySearch, self).extra_context()
        context['title'] = '搜索'
        context['page_num'] = 2
        context['nums'] = cart_count(self.request)
        context['type'] = type_list(self.request)
        return context