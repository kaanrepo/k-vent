from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
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
        return super().setUp()
    
    def test_product_unit_conversion(self):
        product = Product(
            name='test_product',
            unit='kilos',
        )
        product.save()
        self.assertEqual(product.unit_converted, 'kilogram')