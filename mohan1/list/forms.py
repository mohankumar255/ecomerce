from django import forms
from .models import types,items
class register(forms.ModelForm):
    class Meta:
        model=items
        fields='__all__'
class product_add_form(forms.ModelForm):
    class Meta:
        model=items
        fields='__all__'

