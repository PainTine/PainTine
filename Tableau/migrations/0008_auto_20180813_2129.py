# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-13 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Tableau', '0007_auto_20180813_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableau',
            name='RealName',
            field=models.UUIDField(default=uuid.UUID('a417a1db-a3a4-49e3-a0d1-6935e5cb6561'), editable=False, primary_key=True, serialize=False),
        ),
    ]