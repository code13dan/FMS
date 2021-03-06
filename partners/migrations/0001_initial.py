# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, unique=True, verbose_name='Nazwa Firmy')),
                ('address', models.CharField(max_length=100, verbose_name='Siedziba')),
                ('phone', models.PositiveIntegerField(blank=True, null=True, verbose_name='Telefon')),
                ('nip', models.PositiveIntegerField(blank=True, null=True, verbose_name='NIP')),
            ],
        ),
    ]
