from django import forms
from .cities import CITY_CHOICES


class TripForm(forms.Form):
    origin_city = forms.ChoiceField(choices=CITY_CHOICES)
    destination_city = forms.ChoiceField(choices=CITY_CHOICES)
    full_coupe = forms.BooleanField()

