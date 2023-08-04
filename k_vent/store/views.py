from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, InventoryForm, Aform, Aform2
from .models import (
    Product,
    Inventory,
    InventoryOrderItem,
    InventoryOrder,
    ShopOrderItem,
    ShopOrder

)

# Create your views here.


"""
    VIEWS FOR PRODUCT MODEL
"""


def product_list_view(request):
    qs = Product.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'store/product_list.html', context)


def product_detail_view(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    context = {
        'item': obj
    }
    return render(request, 'store/product_detail.html', context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return redirect('product-detail-view', instance.id)
    context = {
        'form': form
    }
    return render(request, 'store/product_create_update.html', context)


def product_update_view(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        instance = form.save()
        return redirect('product-detail-view', instance.id)
    context = {
        'form': form
    }
    return render(request, 'store/product_create_update.html', context)

"""
    VIEWS FOR INVENTORY MODEL
"""


def inventory_list_view(request):
    qs = Inventory.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'store/inventory_list.html', context)


def inventory_detail_view(request, pk):
    obj = get_object_or_404(Inventory, pk=pk)
    context = {
        'item': obj
    }
    return render(request, 'store/inventory_detail.html', context)


def inventory_create_view(request):
    form = InventoryForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return redirect('inventory-detail-view', instance.id)
    context = {
        'form': form
    }
    return render(request, 'store/inventory_create_update.html', context)


def inventory_update_view(request, pk):
    obj = get_object_or_404(Inventory, pk=pk)
    form = InventoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        instance = form.save()
        return redirect('inventory-detail-view', instance.id)
    context = {
        'form': form
    }
    return render(request, 'store/inventory_create_update.html', context)


def test_select2(request):
    form = Aform(request.POST or None)
    form2 = Aform2(request.POST or None)
    if request.method == "POST":
        data = form.data
        print(data)
    context = {
        'form' : form,
        'form2' : form2
    }
    return render(request, 'store/test.html', context)