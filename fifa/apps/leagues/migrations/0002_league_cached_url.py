# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-25 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='cached_url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
