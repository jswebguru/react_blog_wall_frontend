# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-11-29 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import mobovidata_dj.core.storages


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0010_store_shop_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=mobovidata_dj.core.storages.MultipleLevelFileSystemStorage(), upload_to='img_models'),
        ),
        migrations.AddField(
            model_name='model',
            name='synced',
            field=models.BooleanField(default=False),
        ),
    ]