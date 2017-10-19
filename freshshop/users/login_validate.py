# coding=utf-8
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from.models import Userinfo
# 此函数用于作验证登陆
def user_login(func):
    def login_test(request,*args,**kwargs):
        uid = request.session.get('user_id','')
        if uid:
            # 判断数据库是否存在用户
            if Userinfo.objects.filter(id=uid):
                return func(request,*args,**kwargs)
        else:
            # 如果没有登录则返回登陆界面，并用cookie记录登录前的url
            redirect = HttpResponseRedirect(reverse('users:login'))
            redirect.set_cookie('url', request.get_full_path())
            return redirect
    return login_test