# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20171018_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_state',
            name='state',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
