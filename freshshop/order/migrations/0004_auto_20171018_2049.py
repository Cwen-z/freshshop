# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20171018_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_state',
            name='sname',
            field=models.CharField(max_length=1, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81'),
        ),
        migrations.AlterField(
            model_name='order_state',
            name='state',
            field=models.IntegerField(serialize=False, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe7\x8a\xb6\xe6\x80\x81\xe7\xa0\x81', primary_key=True),
        ),
    ]
