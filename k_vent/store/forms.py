from django import forms
from .models import Product, Inventory, InventoryOrder, InventoryOrderItem
from crispy_forms.helper import FormHelper

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'unit', 'price', 'description']


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'unit', 'quantity', 'ideal_quantity']





class Aform2(forms.ModelForm):
    class Meta:
        model = InventoryOrderItem
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm2'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.form_tag = False