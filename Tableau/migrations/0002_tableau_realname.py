# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Tableau', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tableau',
            name='RealName',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
