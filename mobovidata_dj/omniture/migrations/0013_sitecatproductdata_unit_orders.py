# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-20 23:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omniture', '0012_auto_20160920_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitecatproductdata',
            name='unit_orders',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
