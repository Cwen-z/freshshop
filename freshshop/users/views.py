# coding=utf-8
from django.shortcuts import render,redirect
from .models import *
from goods.models import Goodsinfo
from hashlib import sha1
from login_validate import user_login
from django.db import transaction
from task import register_email
from django.core.urlresolvers import reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.views.decorators.http import require_http_methods,require_GET,require_POST
# Create your views here.


@require_GET
def register(request):
    return render(request,'users/register.html',{'title':'注册'})


@require_POST
def register_handler(request):
    post = request.POST
    user = Userinfo()
    name = post.get('user_name')
    phone = post.get('phone')
    user.uname = name
    pwd1 = post.get('pwd')
    pwd2 = post.get('cpwd')
    if pwd1 != pwd2:
        return render(request,'users/register.html')
    m = sha1()
    m.update(pwd1)
    pwd = m.hexdigest()
    user.upwd = pwd
    email = post.get('email')
    user.uemail = email
    user.uphone = phone
    user.save()
    # register_email.delay(name,email)
    return render(request,'users/login.html')


def register_exist(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    user_num = Userinfo.objects.filter(uname=name).count()
    user_phone = Userinfo.objects.filter(uphone=phone).count()
    list3 = [{'user_num':user_num,'user_phone':user_phone}]
    return JsonResponse({'count':list3})


@require_http_methods(['GET','POST'])
def login(request):
    if request.method == 'GET':
        name = request.COOKIES.get('user_name','')
        content = {'title': '登录', 'error_name': 0, 'error_pwd': 0, 'uname': name, 'upwd': ''}
        return render(request,'users/login.html',content)
    post = request.POST
    name = post.get('username')
    pwd = post.get('pwd')
    user = Userinfo.objects.filter(uname=name)
    if len(user) == 0:
        content = {'title':'登录','error_name':1,'error_pwd':0,'uname':name,'upwd':pwd}
        return render(request, 'users/login.html',content)
    else:
        m = sha1()
        m.update(pwd)
        if m.hexdigest() == user[0].upwd:
            url = request.COOKIES.get('url','/')
            red = HttpResponseRedirect(url)
            if post.get('abc') == "1":
                red.set_cookie('user_name',name)
            else:
                red.set_cookie('user_name', '',max_age=-1)
            request.session['user_id'] = user[0].id
            request.session['user_name'] = name
            request.session['uphone'] = user[0].uphone
            request.session.set_expiry(0)
            return red
        else:
            content = {'title': '登录', 'error_name': 0, 'error_pwd': 1, 'uname': name, 'upwd': pwd}
            return render(request, 'users/login.html', content)


@require_GET
def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')

@require_GET
@user_login
def center_info(request):
    id1 = request.session.get('user_id','')
    user = Userinfo.objects.get(id=id1)
    phone = request.session.get('uphone','')
    goods_ids = request.COOKIES.get('goods_ids','')
    if goods_ids != '':
        goods_ids_list = goods_ids.split(',')
        goods_list = []
        for goods_id in goods_ids_list:
            goods_list.append(Goodsinfo.objects.get(id=int(goods_id)))
    else:
        goods_list = ""
    content = {'title':'用户中心','uname':request.session.get('user_name',''),'email':user.uemail,
               'phone_error':0,'phone':phone,'page_num':1,'goods_list':goods_list}
    return render(request, 'users/user_center_info.html', content)


@require_http_methods(['GET','POST'])
@user_login
def center_site(request):
    sid = request.session.get('user_id','')
    user = Userinfo.objects.get(id=sid)
    address = user.addressinfo_set.all()
    return render(request,'users/user_center_site.html',{'title':'用户中心','address': address,'page_num':1})


@require_http_methods(['GET','POST'])
def pro_id(request, p1):
    if p1 == '':
        areas_list = Areasinfo.objects.filter(pid__isnull=True)
    else:
        p2 = int(p1)
        areas_list = Areasinfo.objects.filter(pid_id=p2)
    list1 = []
    for li in areas_list:
        list1.append({'aid': li.id, 'city': li.atitle})
    return JsonResponse({'list1': list1})


@require_POST
def address_handler(request,p1):
    post = request.POST
    pid, cid, did = post.get('pro'), post.get('city'), post.get('dis')
    t1 = Areasinfo.objects.get(id=pid)
    t2 = Areasinfo.objects.get(id=cid)
    t3 = Areasinfo.objects.get(id=did)
    det = post.get('address')
    if p1 != '':
        p2 = int(p1)
        address = Addressinfo.objects.get(id = p2)
    else:
        address = Addressinfo()
    with transaction.atomic():
        address.recipients, address.aphone, address.apostcode = post['shoujian'], post['phone'], post['postcode']
        address.pro, address.city, address.dis, address.detail = t1.atitle, t2.atitle, t3.atitle, det
        address.auser_id = request.session['user_id']
        address.save()
    return redirect(reverse('users:center_site'))


@require_POST
def editor(request,p1):
    p1 = int(p1)
    address = Addressinfo.objects.get(id=p1)
    pro = address.pro
    city = address.city
    dis = address.dis
    areas = Areasinfo.objects
    pro_id = areas.get(atitle=pro).id
    city_id = areas.get(atitle=city).id
    dis_id = areas.get(atitle=dis).id
    det = address.detail
    shoujian = address.recipients
    pc = address.apostcode
    phone = address.aphone
    content = [{'pro_id':pro_id,'city_id':city_id,'dis_id':dis_id,'det':det, 'shoujian':shoujian,'pc':pc,'phone':phone}]
    return JsonResponse({'list1':content})


@require_GET
def del_address(request,p1):
    p2 = int(p1)
    Addressinfo.objects.get(id=p2).delete()
    return redirect(reverse('users:center_site'))