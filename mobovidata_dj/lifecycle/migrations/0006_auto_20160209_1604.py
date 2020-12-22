# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifecycle', '0005_remove_endpoint_endpoint_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rainmaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('modified_dt', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateField(auto_now=True)),
                ('service_type', models.CharField(choices=[('responsys', 'Responsys'), ('mandrill', 'Mandrill')], max_length=50)),
                ('endpoint_name', models.CharField(max_length=50)),
                ('inactivity_threshold', models.IntegerField(default=5)),
                ('funnel_step', models.IntegerField(default=1000)),
                ('lifecycle_messaging_stage', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'lifecycle_rainmaker',
            },
        ),
        migrations.RemoveField(
            model_name='filtercriteria',
            name='endpoint',
        ),
        migrations.DeleteModel(
            name='Endpoint',
        ),
        migrations.DeleteModel(
            name='FilterCriteria',
        ),
    ]