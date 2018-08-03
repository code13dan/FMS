"""Invoices app views"""

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

import json

from .models import Invoice
from .forms import InvoiceForm, ArticleFormSet, SearchForm

from partners.forms import PartnerForm
from partners.models import Partner


def all_invoices(request):
    """Show all invoices"""

    invoices_list = Invoice.objects.select_related('company__company_name')\
        .values('id', 'number', 'company__company_name', 'amount_gross',
                'company_id', 'payment_date')

    paginator = Paginator(invoices_list, 100)
    requested_page = request.GET.get('page')

    try:
        invoices = paginator.page(requested_page)
    except PageNotAnInteger:
        invoices = paginator.page(1)
    except EmptyPage:
        invoices = paginator.page(paginator.num_pages)

    search_form = SearchForm()

    ctx = {'invoices': invoices,
           'search_form': search_form}

    return render(request, 'invoices/all_invoices.html', ctx)


def add_invoice(request):
    """Add invoice"""

    if request.method == 'POST':
        # check if it's new partner or already existing
        try:
            partner_id = int(request.POST['partner_id'])
            partner = Partner.objects.get(pk=partner_id)
            partner_form = PartnerForm(request.POST, instance=partner)
        except ValueError:
            partner_form = PartnerForm(request.POST)

        invoice_form = InvoiceForm(request.POST)
        article_formset = ArticleFormSet(request.POST)
        if article_formset.is_valid() and\
                invoice_form.is_valid() and\
                partner_form.is_valid():
            # save new/changed partner instance
            partner_instance = partner_form.save()
            # get all articles from invoice and save them as JSON string in
            # article field in Invoice model
            articles = []
            for form in article_formset:
                articles.append(
                    {'amount gross': str(form.cleaned_data['amount_gross']),
                     'article_type': form.cleaned_data['article_type'],
                     'destination': form.cleaned_data['destination']}
                    )
            articles_json = json.dumps(articles)
            # create invoice instance with POST partner and articles
            invoice_instance = invoice_form.save(commit=False)
            invoice_instance.company = partner_instance
            invoice_instance.article = articles_json
            invoice_instance.save()
            return redirect('invoices-app:all-url')

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


def show_invoice(request, invoice_id):
    print(invoice_id)
    return redirect('invoices-app:all-url')


def search(request):
    """Return results of search query"""


    raise ValueError('search stop')
    return
