# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-01 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0008_auto_20160424_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='total_bronze',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='total_gold',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='total_informs',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='total_players',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='total_silver',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='total_special',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
