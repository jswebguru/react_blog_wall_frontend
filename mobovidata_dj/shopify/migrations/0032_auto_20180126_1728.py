# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-27 01:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0031_metadataproductattribute_namespace'),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_model_name', models.TextField(blank=True, null=True)),
                ('brand_model_url', models.TextField(blank=True, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=255, null=True)),
                ('brand_url', models.CharField(blank=True, max_length=255, null=True)),
                ('category_name', models.CharField(blank=True, max_length=255, null=True)),
                ('category_url', models.CharField(blank=True, max_length=255, null=True)),
                ('mcid', models.PositiveIntegerField(unique=True)),
                ('model_name', models.CharField(blank=True, max_length=255, null=True)),
                ('model_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'shopify_master_category',
            },
        ),
        migrations.CreateModel(
            name='MasterProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_set_id', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('mpid', models.PositiveIntegerField(unique=True)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'shopify_master_product',
            },
        ),
        migrations.CreateModel(
            name='MetadataCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.Store')),
            ],
            options={
                'db_table': 'shopify_metadata_collection',
            },
        ),
        migrations.CreateModel(
            name='MetadataCollectionAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('error_msg', models.TextField(blank=True, null=True)),
                ('key', models.CharField(db_index=True, max_length=255)),
                ('m_type', models.CharField(choices=[('master_categories', 'Master Categories')], max_length=30)),
                ('namespace', models.CharField(choices=[('master_categories', 'Master Categories')], max_length=50)),
                ('status', models.CharField(choices=[('error', 'Error'), ('synced', 'Synced'), ('unsynced', 'Unsynced')], default='unsynced', max_length=30)),
                ('value', models.TextField(blank=True, null=True)),
                ('collection_metadata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.MetadataCollection')),
            ],
            options={
                'db_table': 'shopify_metadata_collection_attribute',
            },
        ),
        migrations.AlterField(
            model_name='metadataproductattribute',
            name='m_type',
            field=models.CharField(choices=[('description', 'Description'), ('associated_products', 'Associated products'), ('master_product', 'Master Product')], max_length=30),
        ),
        migrations.AlterField(
            model_name='metadataproductattribute',
            name='namespace',
            field=models.CharField(choices=[('product_attributes', 'Product Attributes'), ('variants', 'Variants'), ('master_product', 'Master Product')], max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='metadataproductattribute',
            unique_together=set([('product_metadata', 'key', 'm_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='metadatacollectionattribute',
            unique_together=set([('collection_metadata', 'key', 'm_type')]),
        ),
    ]
