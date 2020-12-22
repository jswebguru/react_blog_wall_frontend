# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-04 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifecycle', '0040_auto_20161004_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='senderlog',
            name='failed_sends',
            field=models.IntegerField(db_column='failed_sends', default=-1),
        ),
        migrations.AddField(
            model_name='senderlog',
            name='successful_sends',
            field=models.IntegerField(db_column='successful_sends', default=-1),
        ),
        migrations.AddField(
            model_name='senderlog',
            name='total_sends',
            field=models.IntegerField(db_column='total_sends', default=-1),
        ),
    ]
