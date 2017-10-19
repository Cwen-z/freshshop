# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('goods', '0002_auto_20171015_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orderdetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oprice', models.DecimalField(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x8d\x95\xe4\xbb\xb7', max_digits=5, decimal_places=2)),
                ('ocount', models.IntegerField(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe6\x95\xb0\xe9\x87\x8f')),
            ],
        ),
        migrations.CreateModel(
            name='Orderinfo',
            fields=[
                ('oid', models.CharField(max_length=18, serialize=False, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\xbc\x96\xe5\x8f\xb7', primary_key=True)),
                ('oaddress', models.CharField(max_length=130, verbose_name=b'\xe6\x94\xb6\xe8\xb4\xa7\xe5\x9c\xb0\xe5\x9d\x80')),
                ('odate', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xb8\x8b\xe5\x8d\x95\xe6\x97\xa5\xe6\x9c\x9f')),
                ('ototal', models.DecimalField(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe6\x80\xbb\xe9\xa2\x9d', max_digits=6, decimal_places=2)),
                ('ostate', models.IntegerField(default=1, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81')),
            ],
        ),
        migrations.CreateModel(
            name='Payway',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pname', models.CharField(max_length=10, verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe6\x96\xb9\xe5\xbc\x8f')),
                ('pway', models.IntegerField(verbose_name=b'\xe6\x95\xb0\xe5\xad\x97\xe7\xa0\x81')),
            ],
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='opay',
            field=models.ForeignKey(verbose_name=b'\xe6\x94\xaf\xe4\xbb\x98\xe6\x96\xb9\xe5\xbc\x8f', to='order.Payway'),
        ),
        migrations.AddField(
            model_name='orderinfo',
            name='ouser',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to='users.Userinfo'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='dorder',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\xbc\x96\xe5\x8f\xb7', to='order.Orderinfo'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='ogoods',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x95\x86\xe5\x93\x81', to='goods.Goodsinfo'),
        ),
    ]
