# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-23 20:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lifecycle', '0017_remove_responsys_campaign_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ActiveCartInfoFilter2',
        ),
    ]
