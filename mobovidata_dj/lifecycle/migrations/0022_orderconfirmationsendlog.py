# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-20 00:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifecycle', '0021_pdpbrowseabandoninfofilter'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderConfirmationSendLog',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('response', models.IntegerField()),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
