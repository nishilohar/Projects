# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-04 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_questionandanswer_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionandanswer',
            name='question',
            field=models.CharField(max_length=100),
        ),
    ]
