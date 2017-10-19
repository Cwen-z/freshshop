# coding=utf-8
from django.db import models


# Create your models here.
# 定义购物车模型，与用户和商品皆为一对多的关系,count为用户购买的某商品数量
class Carinfo(models.Model):
    user = models.ForeignKey('users.Userinfo',verbose_name="购买用户")
    goods = models.ForeignKey('goods.Goodsinfo',verbose_name="购买商品")
    counts = models.IntegerField(verbose_name="购买数量")

    def __unicode__(self):
        return str(self.user)