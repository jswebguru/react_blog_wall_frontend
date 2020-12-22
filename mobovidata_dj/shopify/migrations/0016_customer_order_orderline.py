# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-12-20 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0015_auto_20171206_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepts_marketing', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_id', models.CharField(db_index=True, max_length=32)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('orders_count', models.CharField(blank=True, max_length=3, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('total_spent', models.CharField(blank=True, max_length=50, null=True)),
                ('updated_at', models.DateTimeField()),
                ('tags', models.TextField(blank=True, null=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.Store')),
            ],
            options={
                'db_table': 'shopify_customer',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('financial_status', models.CharField(choices=[('pending', 'pending'), ('authorized', 'authorized'), ('partially_paid', 'partially_paid'), ('paid', 'paid'), ('partially_refunded', 'partially_refunded'), ('refunded', 'refunded'), ('voided', 'voided')], max_length=30)),
                ('order_id', models.CharField(db_index=True, max_length=32)),
                ('landing_site', models.TextField(blank=True, null=True)),
                ('name', models.CharField(db_index=True, max_length=32)),
                ('order_number', models.CharField(db_index=True, max_length=32)),
                ('referring_site', models.TextField(blank=True, null=True)),
                ('source_name', models.CharField(blank=True, max_length=50, null=True)),
                ('subtotal_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total_discounts', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('total_tax', models.DecimalField(decimal_places=2, max_digits=9)),
                ('shipping_address_address1', models.CharField(max_length=255)),
                ('shipping_address_address2', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_address_city', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_address_company', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_address_country', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_address_first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping_address_last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping_address_latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=8, null=True)),
                ('shipping_address_longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('shipping_address_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('shipping_address_province', models.CharField(blank=True, max_length=100, null=True)),
                ('shipping_address_zip', models.CharField(blank=True, max_length=20, null=True)),
                ('shipping_address_name', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_address_country_code', models.CharField(blank=True, max_length=2, null=True)),
                ('shipping_address_province_code', models.CharField(blank=True, max_length=2, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.Customer')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.Store')),
            ],
            options={
                'db_table': 'shopify_order',
            },
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_id', models.CharField(db_index=True, max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('product_id', models.CharField(blank=True, max_length=32, null=True)),
                ('quantity', models.IntegerField()),
                ('sku', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('variant_id', models.CharField(blank=True, max_length=32, null=True)),
                ('variant_title', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('brand_model', models.CharField(blank=True, max_length=255, null=True)),
                ('total_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.Order')),
            ],
            options={
                'db_table': 'shopify_order_line',
            },
        ),
    ]
