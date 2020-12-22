# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-04 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifecycle', '0037_delete_senderlogmonitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='senderlog',
            name='_sends_failed',
            field=models.IntegerField(db_column='failed_sends', default=0),
        ),
        migrations.AddField(
            model_name='senderlog',
            name='_sends_successful',
            field=models.IntegerField(db_column='successful_sends', default=0),
        ),
        migrations.AddField(
            model_name='senderlog',
            name='_sends_total',
            field=models.IntegerField(db_column='total_sends', default=0),
        ),
    ]