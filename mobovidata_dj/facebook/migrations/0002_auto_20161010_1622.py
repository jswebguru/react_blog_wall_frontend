# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-10 23:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('activate', 'Activate'), ('pause', 'Pause')], max_length=16)),
                ('reason', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdOptimizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('manual', 'Manual - Notify, but dont make changes'), ('automatic', 'Automatic')], default='manual', max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=128)),
                ('product_json', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OptimizeCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('if_the', models.CharField(choices=[('clicks', 'Clicks'), ('add_to_cart', 'Add To Cart'), ('add_payment_info', 'Add Payment Info'), ('spend', 'Spend'), ('sales', 'Conversions'), ('cost_per_sale', 'Cost Per Sale')], max_length=16)),
                ('check_type', models.CharField(choices=[('eq', '='), ('gt', '>'), ('gte', '>='), ('lt', '<'), ('lte', '<=')], max_length=16)),
                ('value', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OptimizeNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(choices=[('activate', 'Activate'), ('pause', 'Pause')], max_length=16)),
                ('automatic', models.BooleanField(default=False)),
                ('performed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OptimizeRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('disabled', 'Disabled'), ('manual', 'Manual - Notify, but dont make changes'), ('automatic', 'Automatic')], default='manual', max_length=16)),
                ('applies_to', models.CharField(choices=[('all', 'All ads'), ('today', 'Ads started today'), ('not_today', 'Ads not started today')], max_length=16)),
                ('action', models.CharField(choices=[('activate', 'Activate'), ('pause', 'Pause')], max_length=16)),
                ('match_rules', models.CharField(choices=[('all', 'Match all rules'), ('any', 'Match any rules')], default='all', max_length=16)),
                ('checks', models.ManyToManyField(to='facebook.OptimizeCheck')),
            ],
        ),
        migrations.AddField(
            model_name='facebookad',
            name='ad_id',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='productreport',
            name='ad_obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facebook.FacebookAd'),
        ),
        migrations.AddField(
            model_name='optimizenotification',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='facebook.FacebookAd'),
        ),
        migrations.AddField(
            model_name='optimizenotification',
            name='optimizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='facebook.AdOptimizer'),
        ),
        migrations.AddField(
            model_name='optimizenotification',
            name='rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='facebook.OptimizeRule'),
        ),
        migrations.AddField(
            model_name='optimizenotification',
            name='window',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='facebook.AdStatWindow'),
        ),
        migrations.AddField(
            model_name='advertisedproduct',
            name='ad_objs',
            field=models.ManyToManyField(related_name='product_objs', to='facebook.FacebookAd'),
        ),
        migrations.AddField(
            model_name='adstatwindow',
            name='ad_obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facebook.FacebookAd'),
        ),
        migrations.AddField(
            model_name='adoptimizer',
            name='rules',
            field=models.ManyToManyField(to='facebook.OptimizeRule'),
        ),
        migrations.AddField(
            model_name='adaction',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facebook.FacebookAd'),
        ),
        migrations.AddField(
            model_name='adaction',
            name='performing_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
