# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-01 14:25
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
                ('enter_date', models.DateField(default=django.utils.timezone.now, verbose_name='Wprowadzona')),
                ('number', models.CharField(max_length=50, unique=True, verbose_name='Numer faktury')),
                ('type', models.CharField(choices=[('K', 'Kosztowa'), ('P', 'Przychodowa')], default='K', max_length=1, verbose_name='Rodzaj faktury')),
                ('article', models.TextField(null=True)),
                ('invoice_date', models.DateField(verbose_name='Data wystawienia')),
                ('due_date', models.DateField(verbose_name='Data płatności')),
                ('payment_date', models.DateField(blank=True, null=True, verbose_name='Data uregulowania')),
                ('payment_type', models.CharField(blank=True, choices=[('P', 'Przelew'), ('G', 'Gotówka')], default='P', max_length=1, null=True, verbose_name='Forma płatności')),
                ('amount_vat', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Kwota VAT')),
                ('amount_gross', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Kwota brutto')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner', verbose_name='Firma')),
            ],
        ),
    ]
