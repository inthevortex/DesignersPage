# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-12 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designers', '0004_designers_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designers',
            name='address',
        ),
        migrations.RemoveField(
            model_name='designers',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='designers',
            name='design',
        ),
        migrations.RemoveField(
            model_name='designers',
            name='email',
        ),
        migrations.RemoveField(
            model_name='designers',
            name='firmname',
        ),
        migrations.RemoveField(
            model_name='designers',
            name='name',
        ),
        migrations.RemoveField(
            model_name='designers',
            name='points',
        ),
        migrations.AddField(
            model_name='designers',
            name='password',
            field=models.CharField(max_length=8, null=True),
        ),
    ]