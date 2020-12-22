# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-10 01:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lifecycle', '0047_searchabandon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchAbandonFilter',
            fields=[
                ('filter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='lifecycle.Filter')),
            ],
            options={
                'abstract': False,
            },
            bases=('lifecycle.filter',),
        ),
    ]
