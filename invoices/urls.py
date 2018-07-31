"""Invoices app urls"""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^all$', views.all_invoices, name='all-url'),
    url(r'^add$', views.add_invoice, name='add-url'),
]
