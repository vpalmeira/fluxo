# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-07 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='company_owns',
        ),
        migrations.AddField(
            model_name='device',
            name='owner',
            field=models.CharField(default='A1', max_length=50),
            preserve_default=False,
        ),
    ]
