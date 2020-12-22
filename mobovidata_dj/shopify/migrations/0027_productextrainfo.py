# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-24 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0026_auto_20180124_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductExtraInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shopify.Product')),
            ],
            options={
                'db_table': 'shopify_product_extra_info',
            },
        ),
    ]