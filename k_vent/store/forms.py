from django import forms
from .models import Product, Inventory, InventoryOrder, InventoryOrderItem
from django_select2 import forms as s2forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'unit', 'price', 'description']


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'unit', 'quantity', 'ideal_quantity']


class ProductWidget(s2forms.ModelSelect2Widget):
    search_fields=[
        'name__icontains',
    ]

class Aform(forms.ModelForm):
    class Meta:
        model = InventoryOrderItem
        fields ='__all__'
        widgets ={
            'product' : ProductWidget
        }
    