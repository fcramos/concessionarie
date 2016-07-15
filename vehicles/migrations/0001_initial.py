# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 02:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='nome')),
            ],
            options={
                'verbose_name': 'Montadora',
                'ordering': ['name'],
                'verbose_name_plural': 'Montadora',
            },
        ),
    ]
