# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucketlistapi', '0002_remove_review_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucket',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
