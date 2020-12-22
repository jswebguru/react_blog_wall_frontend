# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-15 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0015_auto_20160625_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='first_visit_created_dt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='first_visit_product_fullid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='first_visit_url_parameters',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='customerorder',
            name='first_visit_url_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
