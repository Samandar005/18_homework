from django.shortcuts import render, get_object_or_404

from products.models import Product
from .models import Order


def order_list(request):
    orders = Order.objects.all()
    ctx = {'orders': orders}
    return render(request, 'orders/list.html', ctx)


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    products = Product.objects.all()
    ctx = {'order': order, 'products': products}
    return render(request, 'orders/detail.html', ctx)
