# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-11-20 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0009_brand_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='shop_url',
            field=models.CharField(default='', max_length=400),
            preserve_default=False,
        ),
    ]