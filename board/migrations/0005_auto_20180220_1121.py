# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-20 02:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='file',
            new_name='image',
        ),
    ]
