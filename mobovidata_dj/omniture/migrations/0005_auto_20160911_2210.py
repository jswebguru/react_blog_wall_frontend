# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-09-12 05:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omniture', '0004_auto_20160911_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitecatproductdata',
            name='date',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='sitecatproductdata',
            name='page_views',
            field=models.IntegerField(default=0),
        ),
    ]