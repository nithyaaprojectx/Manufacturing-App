from django import forms
from .models import Manufacturer

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'expertise', 'notes']
