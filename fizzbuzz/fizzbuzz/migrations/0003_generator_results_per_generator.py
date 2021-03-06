# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-13 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fizzbuzz', '0002_divisor_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='generator',
            name='results_per_generator',
            field=models.IntegerField(default=20, help_text='Since the length of generated string for a generator is unlimited, we have to set a maximum numberof results to return. '),
            preserve_default=False,
        ),
    ]
