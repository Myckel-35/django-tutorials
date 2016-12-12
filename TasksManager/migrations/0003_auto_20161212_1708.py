# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TasksManager', '0002_auto_20161212_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='app_user',
        ),
        migrations.AddField(
            model_name='task',
            name='developer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='TasksManager.Developer', verbose_name='User'),
        ),
    ]
