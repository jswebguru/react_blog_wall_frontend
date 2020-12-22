# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-27 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('responsys', '0014_auto_20161102_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiidEmail',
            fields=[
                ('riid', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('email', models.CharField(max_length=128)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'riid_email',
            },
        ),
    ]