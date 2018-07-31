"""Partners app models"""

from django.db import models


class Partner(models.Model):
    """Partner model"""
    company_name = models.CharField(max_length=100, unique=True, verbose_name='Nazwa Firmy')
    address = models.CharField(max_length=100, verbose_name='Siedziba')
    phone = models.PositiveIntegerField(null=True, blank=True, verbose_name='Telefon')
    nip = models.PositiveIntegerField(null=True, blank=True, verbose_name='NIP')

    def __str__(self):
        return self.company_name
