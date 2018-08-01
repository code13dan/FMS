"""Partners app forms"""

from django import forms

from . import models


class PartnerForm(forms.ModelForm):
    """Adding partner form"""
    partner_id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = models.Partner
        fields = '__all__'
        widgets = {
            'phone': forms.TextInput,
            'nip': forms.TextInput,
        }


class DeleteForm(forms.Form):
    """Deleting partner form"""
    confirmation = forms.BooleanField(label='Odpowiedź')
