# coding=utf-8
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# 此函数用于作验证登陆
def user_login(func):
    def login_test(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            # 返回views函数
            return func(request,*args,**kwargs)
        else:
            # 如果没有登录则返回登陆界面，并用cookie记录登录前的url
            redirect = HttpResponseRedirect(reverse('users:login'))
            redirect.set_cookie('url', request.get_full_path())
            return redirect
    return login_test