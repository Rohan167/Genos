# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-26 03:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animes', '0011_auto_20190104_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]