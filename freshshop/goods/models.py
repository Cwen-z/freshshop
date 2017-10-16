# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Typeinfo(models.Model):
    title = models.CharField(max_length=20, verbose_name='名称')
    isDelete = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Goodsinfo(models.Model):
    gtitle = models.CharField(max_length=20, verbose_name='名称')
    gpic = models.ImageField(upload_to='goods/', verbose_name='图片')
    gprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='单价')
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20, default='500g', verbose_name='单位')
    gclick = models.IntegerField(verbose_name='点击量')
    gdetail = models.CharField(max_length=100, verbose_name='简介')
    grepertory = models.IntegerField(verbose_name='库存')
    gcontent = HTMLField(verbose_name='详情介绍')
    gtype = models.ForeignKey(Typeinfo, verbose_name='类别')

    def __unicode__(self):
        return self.gtitle