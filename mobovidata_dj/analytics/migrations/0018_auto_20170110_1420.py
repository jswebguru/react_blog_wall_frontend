# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-10 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0017_customerdevice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdevice',
            name='riid',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
    ]