# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-02-15 23:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0004_auto_20170214_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='model_pic',
        ),
    ]
