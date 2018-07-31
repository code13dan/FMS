# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-27 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_date', models.DateField(default=django.utils.timezone.now)),
                ('number', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('K', 'Kosztowa'), ('P', 'Przychodowa')], max_length=1)),
                ('article', models.TextField()),
                ('invoice_date', models.DateField()),
                ('due_date', models.DateField()),
                ('payment_date', models.DateField()),
                ('payment_type', models.CharField(choices=[('P', 'Przelew'), ('G', 'Gotówka')], max_length=1)),
                ('amount_vat', models.DecimalField(decimal_places=2, max_digits=8)),
                ('amount_gross', models.DecimalField(decimal_places=2, max_digits=8)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner')),
            ],
        ),
    ]
