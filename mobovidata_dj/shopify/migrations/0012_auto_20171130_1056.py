# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-11-30 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0011_auto_20171129_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='adaptor_type',
            field=models.CharField(blank=True, choices=[('apple-30-pin', 'apple-30-pin'), ('apple-8-pin', 'apple-8-pin'), ('lg-chocolate', 'lg-chocolate'), ('micro-usb', 'micro-usb'), ('usb-type-c', 'usb-type-c'), ('mini-usb', 'mini-usb')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='model',
            name='error',
            field=models.TextField(blank=True, null=True),
        ),
    ]
