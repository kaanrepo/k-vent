from django.db import models
from django.conf import settings
from .utils import number_str_to_float
from .validators import validate_unit_of_measure
import pint
from pathlib import Path
from django.utils import timezone
from datetime import datetime
from django.db.models import F, ExpressionWrapper, FloatField
from django.urls import reverse

BASE_DIR = Path(__file__).resolve().parent.parent.parent
# Create your models here.

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=50, validators=[
                            validate_unit_of_measure])
    unit_converted = models.CharField(max_length=20, null=True, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=100)
    description = models.CharField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        ureg = pint.UnitRegistry()
        ureg.load_definitions(BASE_DIR / 'my_def.txt')
        self.unit_converted = str(ureg[f'{self.unit}']).split()[1]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product-detail-view", kwargs={"pk": self.pk})

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class InventoryManager(models.Manager):

    def to_ideal(self):
        """
            Function to generate a queryset for an Ideal Inventory Order.
        """
        qs = Inventory.objects.filter(ideal_quantity__isnull=False)
        qs = qs.annotate(difference_to_ideal=ExpressionWrapper(
            F('ideal_quantity') - F('quantity_as_float'),
            output_field=FloatField()
        )
        )
        qs = qs.filter(difference_to_ideal__gt=0)
        return qs


class Inventory(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.SET_NULL, null=True)
    unit = models.CharField(max_length=20, validators=[
                            validate_unit_of_measure])
    unit_converted = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True)
    ideal_quantity = models.FloatField(blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = InventoryManager()

    class Meta:
        verbose_name_plural = 'Inventory'

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        ureg = pint.UnitRegistry()
        ureg.load_definitions(BASE_DIR / 'my_def.txt')
        self.unit_converted = str(ureg[f'{self.unit}']).split()[1]
        super().save(*args, **kwargs)

    def __repr__(self):
        return self.product.name

    def __str__(self):
        return self.product.name

class InventoryOrderManager(models.Manager):

    def unrealized_orders(self):
        query = InventoryOrder.objects.filter(
            realized=False).order_by('-updated')
        return query

    def realized_orders(self):
        query = InventoryOrder.objects.filter(
            realized=True).order_by('-updated')
        return query



class InventoryOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    realized = models.BooleanField(default=False)
    realized_date = models.DateTimeField(null=True, blank=True, default=None)
    realized_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                    null=True, default=None, related_name='realized_inventory_orders')

    objects = InventoryOrderManager()

    def __repr__(self):
        return f"{self.user.username} - {self.created}"

    def __str__(self):
        return f"{self.user.username} - {self.created}"

    def realize_order(self):
        if self.realized == True:
            return None
        ureg = pint.UnitRegistry()
        for item in self.order_items.all():
            item_mass = ureg(f'{item.quantity} {item.unit_converted}')
            try:
                inventory_item = Inventory.objects.get(product=item.product)
                if inventory_item.unit is None:
                    inventory_item.unit = item.unit_converted
                    inventory_item.unit = item.unit_converted
                inventory_item_mass = ureg(
                    f'{inventory_item.quantity} {inventory_item.unit_converted}')
                new_mass = inventory_item_mass + item_mass
                inventory_item.quantity = str(new_mass).split()[0]
                inventory_item.save()
                self.realized = True
                self.realized_date = timezone.now()
                self.save()
            except Inventory.DoesNotExist:
                inventory_item = Inventory(
                    product=item.product,
                    unit=item.unit,
                    quantity=item.quantity
                )
                inventory_item.save()
                self.realized = True
                self.realized_date = timezone.now()
                self.save()
            except:
                pass


class InventoryOrderItem(models.Model):
    inventory_order = models.ForeignKey(InventoryOrder, on_delete=models.SET_NULL, null=True, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    unit = models.CharField(max_length=20, validators=[
                            validate_unit_of_measure])
    unit_converted = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.CharField(max_length=20)

    def __repr__(self):
        return f'{self.product.name} - {self.quantity} {self.unit_converted}'

    def __str__(self):
        return f'{self.product.name} - {self.quantity} {self.unit_converted}'

    def save(self, *args, **kwargs):
        ureg = pint.UnitRegistry()
        ureg.load_definitions(BASE_DIR / 'my_def.txt')
        self.unit_converted = str(ureg[f'{self.unit}']).split()[1]
        super().save(*args, **kwargs)





class ShopOrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    unit = models.CharField(max_length=20, validators=[
                            validate_unit_of_measure])
    unit_converted = models.CharField(max_length=20, null=True, blank=True)
    quantity = models.CharField(max_length=20)

    def __repr__(self):
        return f'{self.product.name} - {self.quantity} {self.unit_converted}'

    def __str__(self):
        return f'{self.product.name} - {self.quantity} {self.unit_converted}'

    def save(self, *args, **kwargs):
        ureg = pint.UnitRegistry()
        ureg.load_definitions(BASE_DIR / 'my_def.txt')
        self.unit_converted = str(ureg[f'{self.unit}']).split()[1]
        super().save(*args, **kwargs)


class ShopOrderManager(models.Manager):

    def unrealized_orders(self):
        query = ShopOrder.objects.filter(realized=False).order_by('-updated')
        return query

    def realized_orders(self):
        query = ShopOrder.objects.filter(realized=True).order_by('-updated')
        return query


class ShopOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(ShopOrderItem)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    realized = models.BooleanField(default=False)
    realized_date = models.DateTimeField(null=True, blank=True, default=None)
    realized_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, default=None, related_name='realized_shop_orders')

    objects = ShopOrderManager()

    def realize_order(self):
        if self.realized == True:
            return None
        ureg = pint.UnitRegistry()
        for item in self.items.all():
            item_mass = ureg(f'{item.quantity} {item.unit_converted}')
            try:
                inventory_item = Inventory.objects.get(product=item.product)
                inventory_item_mass = ureg(
                    f'{inventory_item.quantity} {inventory_item.unit_converted}')
                new_mass = inventory_item_mass - item_mass
                inventory_item.quantity = str(new_mass).split()[0]
                inventory_item.save()
                self.realized = True
                self.realized_date = timezone.now()
                self.save()
            except Inventory.DoesNotExist:
                inventory_item = Inventory(
                    product=item.product,
                    unit=item.unit,
                    quantity=f'-{item.quantity}'
                )
                inventory_item.save()
                self.realized = True
                self.realized_date = timezone.now()
                self.save()
            except:
                pass
