# coding=utf-8
from django.db import models

# Create your models here.
# 创建订单类模型，用于获取订单信息并维护
class Orderinfo(models.Model):
    oid = models.CharField(max_length=18,primary_key=True,verbose_name="订单编号")
    ouser = models.ForeignKey('users.Userinfo',verbose_name="用户")
    oaddress = models.CharField(max_length=130,verbose_name="收货地址")
    odate = models.DateTimeField(auto_now=True,verbose_name="下单日期")
    ototal = models.DecimalField(max_digits=6,decimal_places=2,verbose_name="订单总额")
    opay = models.ForeignKey('Payway',verbose_name="支付方式")
    ostate = models.ForeignKey('Order_state',verbose_name="订单状态") # 订单状态，1为未支付，2为已支付，未发货，3为已支付并发货，4为取消订单

# 创建订单详情，与订单类关联
class Orderdetail(models.Model):
    dorder = models.ForeignKey('Orderinfo',verbose_name="订单编号")
    ogoods = models.ForeignKey('goods.Goodsinfo',verbose_name="订单商品")
    oprice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name="订单单价")
    ocount = models.IntegerField(verbose_name="订单数量")


# 创建支付方式模型，用于获取用户所选支付方式
class Payway(models.Model):
    pname = models.CharField(max_length=10,verbose_name="支付方式")
    pway = models.IntegerField(verbose_name="数字码") # 1：货到付款 2：微信支付 3：支付宝支付 4：银行卡支付

    def __unicode__(self):
        return self.pname

class Order_state(models.Model):
    state = models.IntegerField(primary_key=True,verbose_name='订单状态码')
    sname = models.CharField(max_length=10,verbose_name='订单状态')

    def __unicode__(self):
        return self.sname