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
            name='Carinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('counts', models.IntegerField()),
                ('goods', models.ForeignKey(to='goods.Goodsinfo')),
                ('user', models.ForeignKey(to='users.Userinfo')),
            ],
        ),
    ]
