from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """"""
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'county', 'postcode', 'town_or_city',
    'street_address1', 'street_address2', 'country')

    def __init__(self, **args, **kwargs):
        """Set placeholders and autofocus on first field"""
        super().__init__(**args, **kwargs)

        self.field['full_name'].widget.attrs['autofocus'] = True

        # add stripe-style-input styling to base.css
        self.field[field].widget.attrs['class'] = 'stripe-style-input'