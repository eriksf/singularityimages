# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_image_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]