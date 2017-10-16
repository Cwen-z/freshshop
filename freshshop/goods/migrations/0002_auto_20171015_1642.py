# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gcontent',
            field=tinymce.models.HTMLField(verbose_name=b'\xe8\xaf\xa6\xe6\x83\x85\xe4\xbb\x8b\xe7\xbb\x8d'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gdetail',
            field=models.CharField(max_length=100, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to=b'goods/', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gprice',
            field=models.DecimalField(verbose_name=b'\xe5\x8d\x95\xe4\xbb\xb7', max_digits=5, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='grepertory',
            field=models.IntegerField(verbose_name=b'\xe5\xba\x93\xe5\xad\x98'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtitle',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(verbose_name=b'\xe7\xb1\xbb\xe5\x88\xab', to='goods.Typeinfo'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gunit',
            field=models.CharField(default=b'500g', max_length=20, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d'),
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='title',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
