# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storage101', '0002_remove_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=50, null=True, verbose_name='email'),
        ),
    ]