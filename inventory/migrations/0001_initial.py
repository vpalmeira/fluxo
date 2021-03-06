# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-07 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('reference_code', models.CharField(max_length=15)),
                ('category', models.CharField(max_length=50)),
                ('company_owns', models.BooleanField()),
                ('location', models.CharField(max_length=100)),
                ('sell_value', models.FloatField()),
                ('buy_value', models.FloatField()),
            ],
        ),
    ]
