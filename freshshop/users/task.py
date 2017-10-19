# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from django.core.mail import send_mail
from celery import task
from django.conf import settings

@task
def register_email(username, email):
    subject = '欢迎使用dailyfresh'
    message = '恭喜您，成功注册为dailyfresh会员！  账户名为:'+username
    recipient_list = [email]
    send_mail(subject=subject, message=message, from_email=settings.EMAIL_FROM,recipient_list=recipient_list)
