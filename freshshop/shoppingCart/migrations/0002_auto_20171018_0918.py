# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingCart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinfo',
            name='counts',
            field=models.IntegerField(verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe6\x95\xb0\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='goods',
            field=models.ForeignKey(verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe5\x95\x86\xe5\x93\x81', to='goods.Goodsinfo'),
        ),
        migrations.AlterField(
            model_name='carinfo',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe7\x94\xa8\xe6\x88\xb7', to='users.Userinfo'),
        ),
    ]
