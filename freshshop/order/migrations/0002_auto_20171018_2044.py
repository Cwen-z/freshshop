# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_state',
            fields=[
                ('state', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('sname', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='ostate',
            field=models.ForeignKey(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81', to='order.Order_state'),
        ),
    ]
