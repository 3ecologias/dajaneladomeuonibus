# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20161019_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonials',
            name='body',
        ),
        migrations.AddField(
            model_name='testimonials',
            name='instagram_user',
            field=models.TextField(blank=True, null=True),
        ),
    ]
