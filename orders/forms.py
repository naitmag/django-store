import re

from django import forms
from django.utils.translation import gettext_lazy as _


class CreateOrderForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(choices=[('0', False),
                                                   ('1', True)])
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(choices=[('0', 'False'),
                                                ('1', 'True')])

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        allowed_chars = '()- '
        table = str.maketrans('', '', allowed_chars)

        data = data.translate(table)

        if not data.isdigit():
            raise forms.ValidationError(_('The phone number must contain only digits'))

        pattern = re.compile(r'^\d{10}$')
        if not pattern.match(data):
            raise forms.ValidationError(_('Incorrect phone number format'))

        return data
