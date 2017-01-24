# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 02:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0002_description_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='id',
        ),
        migrations.AlterField(
            model_name='description',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='course_app.Course'),
        ),
    ]
