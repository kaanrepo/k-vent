from django.db import models
from django.conf import settings
from .utils import number_str_to_float
from .validators import validate_unit_of_measure
import pint
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
# Create your models here.

User = settings.AUTH_USER_MODEL 

class Product(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])
    unit_converted = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        ureg = pint.UnitRegistry()
        ureg.load_definitions(BASE_DIR / 'my_def.txt')
        self.unit_converted = str(ureg[f'{self.unit}']).split()[1]
        super().save(*args, **kwargs)

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return self.name


class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    unit = models.CharField(max_length=20, validators=[validate_unit_of_measure])
    unit_converted = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True)
    ideal_quantity = models.FloatField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Inventory'

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float , qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        ureg = pint.UnitRegistry()
        ureg.load_definitions(BASE_DIR / 'my_def.txt')
        self.unit_converted = str(ureg[f'{self.default_unit}']).split()[1]
        super().save(*args, **kwargs)
    
    def __repr__(self):
        return self.product.name
    
    def __str__(self):
        return self.product.name


class InventoryOrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    unit = models.CharField(max_length=20, validators=[validate_unit_of_measure])
    unit_converted = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.CharField(max_length=20)

    def __repr__(self):
        return self.product.name
    
    def __str__(self):
        return self.product.name

    def save(self, *args, **kwargs):
        ureg = pint.UnitRegistry()
        ureg.load_definitions(BASE_DIR / 'my_def.txt')
        self.unit_converted = str(ureg[f'{self.default_unit}']).split()[1]
        super().save(*args, **kwargs)   


class InventoryOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(InventoryOrderItem)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    realized = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float , qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)

    def __repr__(self):
        return f"{self.user.username} - {self.created} - {self.items.count()}"
    
    def __str__(self):
        return f"{self.user.username} - {self.created} - {self.items.count()}"


class ShopOrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    unit = models.CharField(max_length=20, validators=[validate_unit_of_measure])
    unit_converted = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.CharField(max_length=20)

    def __repr__(self):
        return self.product.name
    
    def __str__(self):
        return self.product.name
    
    def save(self, *args, **kwargs):
        ureg = pint.UnitRegistry()
        ureg.load_definitions(BASE_DIR / 'my_def.txt')
        self.unit_converted = str(ureg[f'{self.unit}']).split()[1]
        super().save(*args, **kwargs)        

class ShopOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(ShopOrderItem)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    realized = models.BooleanField(default=False)