# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-15 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_auto_20160414_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='GmailAdEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('riid', models.IntegerField()),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
