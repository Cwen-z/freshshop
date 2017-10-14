# coding=utf-8
from django.core.mail import send_mail
from celery import task
from django.conf import settings

@task
def register_email(username, email):
    subject = '欢迎来到dailyfresh'
    message = '恭喜您，成功注册dailyfresh会员！您的用户名为'+username+', 请牢记！'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(
        subject=subject, message=message, from_email=from_email,
        recipient_list=recipient_list)
