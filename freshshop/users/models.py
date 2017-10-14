# coding:utf-8
from django.db import models

# Create your models here.


class Userinfo(models.Model):
    uname = models.CharField(max_length=20,verbose_name="用户名")
    upwd = models.CharField(max_length=40,verbose_name="密码")
    uemail = models.CharField(max_length=40,verbose_name="邮箱", default='')
    uphone = models.CharField(max_length=11,verbose_name="手机号码", default='')

    class Meta:
        db_table = 'Userinfo'

    def __unicode__(self):
        return self.uname


class Addressinfo(models.Model):
    pro = models.CharField(max_length=20, verbose_name="省", default='')
    city = models.CharField(max_length=20, verbose_name="市", default='')
    dis = models.CharField(max_length=20, verbose_name="区", default='')
    detail = models.CharField(max_length=30, verbose_name="详细地址", default='')
    recipients = models.CharField(max_length=20,verbose_name="收件人", default='')
    apostcode = models.CharField(max_length=6,verbose_name="邮政编码", default='')
    aphone = models.CharField(max_length=11, verbose_name="手机号码", default='')
    auser = models.ForeignKey('Userinfo')

    class Meta:
        db_table = 'UserAddress'

class Areasinfo(models.Model):
    atitle = models.CharField(max_length=20, verbose_name="省/市/区")
    pid = models.ForeignKey('self', null=True, blank=True)