"""Invoices app views"""

from django.shortcuts import render, redirect
from django.contrib import messages

import json

from .models import Invoice
from .forms import InvoiceForm, ArticleFormSet

from partners.forms import PartnerForm
from partners.models import Partner


def all_invoices(request):
    """Show all invoices"""

    articles_json = Invoice.objects.values_list('article', flat=True)
    articles = [json.loads(article) for article in articles_json]
    ctx = {'invoices': articles}

    return render(request, 'invoices/all_invoices.html', ctx)


def add_invoice(request):
    """Add invoice"""

    if request.method == 'POST':
        invoice_form = InvoiceForm(request.POST)
        article_formset = ArticleFormSet(request.POST)
        partner_form = PartnerForm(request.POST)
        if article_formset.is_valid() and\
                invoice_form.is_valid() and\
                partner_form.is_valid():
            # get all articles from invoice and save them as JSON string in
            # article field in Invoice model
            articles = []
            for form in article_formset:
                articles.append(
                    {'amount gross': str(form.cleaned_data['amount_gross']),
                     'article_type': form.cleaned_data['article_type'],
                     'destination': form.cleaned_data['destination']}
                    )
            articles = json.dumps(articles)
            raise ValueError()

    else:
        article_formset = ArticleFormSet()
        invoice_form = InvoiceForm()
        partner_form = PartnerForm()

    # create partners list for page js searching purpose
    partners_list = Partner.objects.order_by('company_name')\
        .values('id', 'company_name')

    ctx = {'partners_list': partners_list,
           'partner_form': partner_form,
           'article_form_set': article_formset,
           'invoice_form': invoice_form}
    return render(request, 'invoices/add_invoice.html', ctx)
