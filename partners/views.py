"""Partners app views"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Partner
from .forms import PartnerForm, DeleteForm


def all_partners(request):
    """Show list of all partners"""

    partners = Partner.objects.values()
    ctx = {'all_partners': partners}
    return render(request, 'partners/all_partners.html', ctx)


def add_partner(request):
    """Add new partner"""

    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Dodano partnera')
            return redirect('partners-app:all-url')

    else:
        form = PartnerForm()

    ctx = {'form': form}
    return render(request, 'partners/add_partner.html', ctx)


def show_partner(request, partner_id):
    """Show detail information about chosen partner and allow editing
    particular information or delete partner"""

    partner = Partner.objects.get(pk=partner_id)
    partner = model_to_dict(partner)

    ctx = {'partner': partner}
    return render(request, 'partners/show_partner.html', ctx)


def edit_partner(request, partner_id):
    """Edit detail information about chosen partner"""

    partner = Partner.objects.get(pk=partner_id)
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Zapisano zmiany')
            return redirect('partners-app:show-url', partner_id)

    else:
        form = PartnerForm(instance=partner)

    ctx = {
        'form': form,
        'partner_id': partner_id
    }
    return render(request, 'partners/edit_partner.html', ctx)


def delete_partner(request, partner_id):
    """Delete chosen partner"""

    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['confirmation']:
                partner = Partner.objects.get(pk=partner_id)
                partner.delete()
                messages.add_message(request, messages.SUCCESS,
                                     'Partner usunięty')
                return redirect('partners-app:all-url')

    else:
        # return confirmation form of delete action
        form = DeleteForm()

    ctx = {'form': form,
           'partner_id': partner_id,
           }
    return render(request, 'partners/delete_partner.html', ctx)


def get_partner(request, partner_id):
    """Return partner data in json format"""

    partner = Partner.objects.get(pk=partner_id)
    partner = model_to_dict(partner)

    return JsonResponse(partner)
