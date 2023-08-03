from django import forms
from .models import Product, Inventory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'unit', 'price', 'description']


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'unit', 'quantity', 'ideal_quantity']
