from django import forms
from .models import Products
class ProductForm(forms.Form):
    class Meta:
        model = Products
        # fields =

