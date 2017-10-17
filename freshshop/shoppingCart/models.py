# coding=utf-8
from django.db import models


# Create your models here.
# 定义购物车模型，与用户和商品皆为一对多的关系,count为用户购买的某商品数量
class Carinfo(models.Model):
    user = models.ForeignKey('users.Userinfo')
    goods = models.ForeignKey('goods.Goodsinfo')
    counts = models.IntegerField()