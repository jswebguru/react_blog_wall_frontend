# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-20 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0016_customer_order_orderline'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='order_task_run_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
