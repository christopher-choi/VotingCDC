# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0004_auto_20161104_1502'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserLogin',
            new_name='Login',
        ),
    ]