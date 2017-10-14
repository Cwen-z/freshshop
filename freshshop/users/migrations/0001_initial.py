# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addressinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pro', models.CharField(default=b'', max_length=20, verbose_name=b'\xe7\x9c\x81')),
                ('city', models.CharField(default=b'', max_length=20, verbose_name=b'\xe5\xb8\x82')),
                ('dis', models.CharField(default=b'', max_length=20, verbose_name=b'\xe5\x8c\xba')),
                ('detail', models.CharField(default=b'', max_length=30, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x9c\xb0\xe5\x9d\x80')),
                ('recipients', models.CharField(default=b'', max_length=20, verbose_name=b'\xe6\x94\xb6\xe4\xbb\xb6\xe4\xba\xba')),
                ('apostcode', models.CharField(default=b'', max_length=6, verbose_name=b'\xe9\x82\xae\xe6\x94\xbf\xe7\xbc\x96\xe7\xa0\x81')),
                ('aphone', models.CharField(default=b'', max_length=11, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81')),
            ],
            options={
                'db_table': 'UserAddress',
            },
        ),
        migrations.CreateModel(
            name='Areasinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atitle', models.CharField(max_length=20, verbose_name=b'\xe7\x9c\x81/\xe5\xb8\x82/\xe5\x8c\xba')),
                ('pid', models.ForeignKey(blank=True, to='users.Areasinfo', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d')),
                ('upwd', models.CharField(max_length=40, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
                ('uemail', models.CharField(default=b'', max_length=40, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1')),
                ('uphone', models.CharField(default=b'', max_length=11, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81')),
            ],
            options={
                'db_table': 'Userinfo',
            },
        ),
        migrations.AddField(
            model_name='addressinfo',
            name='auser',
            field=models.ForeignKey(to='users.Userinfo'),
        ),
    ]
