# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 17:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_auto_20170125_1739'),
        ('books_app', '0002_review_reviewer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='author',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewer',
        ),
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to='login_app.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book_review', to='books_app.Book'),
            preserve_default=False,
        ),
    ]
