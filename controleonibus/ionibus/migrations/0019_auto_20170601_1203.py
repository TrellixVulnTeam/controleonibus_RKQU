# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-01 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ionibus', '0018_auto_20170601_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circuito',
            name='parte',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B')], max_length=1, verbose_name='Parte'),
        ),
    ]
