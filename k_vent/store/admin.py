from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import (
    Product,
    Inventory,
    InventoryOrderItem,
    InventoryOrder,
    ShopOrderItem,
    ShopOrder

)
# Register your models here.

admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(InventoryOrderItem)
admin.site.register(InventoryOrder)
admin.site.register(ShopOrderItem)
admin.site.register(ShopOrder)

class ShopOrderItemAdmin(admin.ModelAdmin):
    def get_queryset(self,) -> QuerySet[Any]:
        qs = Product.objects.all()
        return qs
    
class InventoryOrderItemAdmin(admin.ModelAdmin):
    def get_queryset(self,) -> QuerySet[Any]:
        qs = Product.objects.all()
        return qs