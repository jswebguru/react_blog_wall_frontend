# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-10 23:45
from __future__ import unicode_literals

from django.db import migrations
import json


def forwards(app, schema):
    FacebookAd = app.get_model('facebook', 'FacebookAd')
    for ad in FacebookAd.objects.all():
        if ad.products:
            try: products = eval(ad.products)
            except:
                try: products = json.loads(ad.products)
                except: products = []
        else: products = []
        ad.products = json.dumps(products)
        ad.save()

def backwards(app, schema):
    FacebookAd = app.get_model('facebook', 'FacebookAd')
    for ad in FacebookAd.objects.all():
        if ad.products:
            try: products = eval(ad.products)
            except:
                try: products = json.loads(ad.products)
                except: products = []
        else: products = []
        ad.products = str(products)
        ad.save()


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_auto_20161010_1622'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards)
    ]
