# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifecycle', '0016_senderlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responsys',
            name='campaign_name',
        ),
    ]
