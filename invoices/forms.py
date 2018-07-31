"""Invoices app forms"""

from django import forms

from .models import Invoice


class InvoiceForm(forms.ModelForm):
    """Adding invoice form"""

    class Meta:
        model = Invoice
        exclude = ['article', 'company']
        widgets = {
            'amount_vat': forms.TextInput,
            'amount_gross': forms.TextInput,
        }


class ArticleForm(forms.Form):
    """Adding article form"""

    DESTINATION_POINTS = (
        ('pap', 'Papugi'),
        ('pz', 'Przystanek Zoo'),
        ('rl', 'Restauracja Letnia'),
        ('zol', 'Zoo Land'),
        ('pR', 'Pan Roman'),
        ('pW', 'Pan Wiesław')
    )

    amount_gross = forms.DecimalField(decimal_places=2,
                                      widget=forms.TextInput,
                                      label='Kwota brutto')
    destination = forms.ChoiceField(choices=DESTINATION_POINTS,
                                    label='Wybierz punkt')
    article_type = forms.CharField(max_length=100,
                                   label='Nazwa grupy')


ArticleFormSet = forms.formset_factory(ArticleForm, max_num=20)
