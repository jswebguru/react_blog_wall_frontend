# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-12 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifecycle', '0042_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderConfirmationEmailsLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('order_updated_at', models.DateTimeField()),
                ('base_grand_total', models.DecimalField(decimal_places=4, max_digits=12)),
                ('response', models.IntegerField()),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
