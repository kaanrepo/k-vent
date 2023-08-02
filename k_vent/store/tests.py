from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.utils import timezone
from .models import (
    Product,
    Inventory,
    InventoryOrderItem,
    InventoryOrder,
    ShopOrderItem,
    ShopOrder

)
# Create your tests here.

User = get_user_model()


class ProductTestCase(TestCase):
    
    def setUp(self):
        self.user_a = User.objects.create_user(username='testuser_a', email='test@test.com', password='abc123')
        self.product_a = Product.objects.create(
            name='object1',
            unit='kilogram',
            price='120'
        )
        self.product_b = Product.objects.create(
            name='object2',
            unit='grams',
            price='50'
        )

        self.inventory_a =Inventory.objects.create(
            product = self.product_a,
            unit = self.product_a.unit,
            quantity= '100'
        )

        self.inventory_order_item_a = InventoryOrderItem.objects.create(
            product = self.product_a,
            unit = 'kg',
            quantity = 100
        )

        self.inventory_order_item_b = InventoryOrderItem.objects.create(
            product = self.product_b,
            unit = 'kg',
            quantity = '120'
        )

        self.inventory_order_a = InventoryOrder(
            user = self.user_a
        )
        self.inventory_order_a.save()
        self.inventory_order_a.items.add(self.inventory_order_item_a, self.inventory_order_item_b)

        self.shop_order_item_a = ShopOrderItem.objects.create(
            product = self.product_a,
            unit = 'kg',
            quantity = 100
        )

        self.shop_order_item_b = ShopOrderItem.objects.create(
            product = self.product_b,
            unit = 'kg',
            quantity = '120'
        )

        self.shop_order_a = ShopOrder(
            user = self.user_a
        )
        self.shop_order_a.save()
        self.shop_order_a.items.add(self.shop_order_item_a, self.shop_order_item_b)


        return super().setUp()
    
    def test_product_unit_conversion(self):
        product = Product(
            name='test_product',
            unit='kilos',
        )
        product.save()
        self.assertEqual(product.unit_converted, 'kilogram')

    def test_realize_inventory_order(self):
        self.assertEqual(self.inventory_a.quantity_as_float, 100)
        self.inventory_order_a.realize_order()
        self.inventory_a = Inventory.objects.get(product=self.product_a)
        self.assertEqual(self.inventory_a.quantity_as_float, 200)

    def test_realize_shop_order(self):
        self.assertEqual(self.inventory_a.quantity_as_float, 100)
        self.shop_order_a.realize_order()
        self.inventory_a = Inventory.objects.get(product=self.product_a)
        self.assertEqual(self.inventory_a.quantity_as_float, 0)

    def test_realize_order_time(self):
        self.inventory_order_a.realize_order()
        self.assertAlmostEqual(self.inventory_order_a.realized_date, timezone.now() ,delta=timezone.timedelta(seconds=2))




    # def test_realize_inventory_order_update(self):
    #     self.inventory_order_a.realize_order()


    