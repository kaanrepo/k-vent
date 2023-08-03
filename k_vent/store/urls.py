from django.urls import path
from .views import(
    product_detail_view,
    product_list_view,
    product_create_view,
    product_update_view,
    inventory_list_view,
    inventory_update_view,
    inventory_detail_view,
    inventory_create_view,
    test_select2
)


urlpatterns = [
    #Urls for Products
    path('products/', product_list_view, name='product-list-view'),
    path('products/<int:pk>/', product_detail_view, name='product-detail-view'),
    path('product/create/', product_create_view, name='product-create-view'),
    path('product/<int:pk>/update/', product_update_view, name='product-update-view'),
    #Urls for Inventory
    path('inventory/', inventory_list_view, name='inventory-list-view'),
    path('inventory/create/', inventory_create_view, name='inventory-create-view'),
    path('inventory/<int:pk>/', inventory_detail_view, name='inventory-detail-view'),
    path('inventory/<int:pk>/update/', inventory_update_view, name='inventory-update-view'),
    #test2
    path('test/', test_select2)
]
