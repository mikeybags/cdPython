# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 05:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='confirm_pw',
        ),
    ]
