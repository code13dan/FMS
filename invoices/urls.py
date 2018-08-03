"""Invoices app urls"""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^all$', views.all_invoices, name='all-url'),
    url(r'^add$', views.add_invoice, name='add-url'),
    url(r'^show/(\d+)', views.show_invoice, name='show-url'),
    url(r'^search$', views.search, name='search-url'),
]
