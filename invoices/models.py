"""Invoices app models"""

from django.db import models
from django.utils import timezone


class Invoice(models.Model):
    """Invoice model"""

    INVOICES_TYPES = (
        ('K', 'Kosztowa'),
        ('P', 'Przychodowa')
    )

    PAYMENT_TYPES = (
        ('P', 'Przelew'),
        ('G', 'Gotówka')
    )

    company = models.ForeignKey('partners.Partner', null=True, blank=True,
                                verbose_name='Firma')
    enter_date = models.DateField(default=timezone.now,
                                  verbose_name='Wprowadzona')
    number = models.CharField(max_length=50, verbose_name='Numer faktury',
                              unique=True)
    type = models.CharField(max_length=1, choices=INVOICES_TYPES, default='K',
                            verbose_name='Rodzaj faktury')
    article = models.TextField(null=True)
    invoice_date = models.DateField(verbose_name='Data wystawienia')
    due_date = models.DateField(verbose_name='Data płatności')
    payment_date = models.DateField(verbose_name='Data uregulowania',
                                    blank=True, null=True)
    payment_type = models.CharField(max_length=1, choices=PAYMENT_TYPES,
                                    default='P', verbose_name='Forma płatności',
                                    blank=True, null=True)
    amount_vat = models.DecimalField(max_digits=8, decimal_places=2,
                                     verbose_name='Kwota VAT', blank=True,
                                     null=True)
    amount_gross = models.DecimalField(max_digits=8, decimal_places=2,
                                       verbose_name='Kwota brutto')
