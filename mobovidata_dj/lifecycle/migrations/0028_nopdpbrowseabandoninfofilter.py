# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-05 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifecycle', '0027_auto_20160511_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoPDPBrowseAbandonInfoFilter',
            fields=[
                ('filter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='lifecycle.Filter')),
            ],
            options={
                'abstract': False,
            },
            bases=('lifecycle.filter',),
        ),
    ]
