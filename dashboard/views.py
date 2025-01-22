from django.shortcuts import render
from categories.models import Category
from orders.models import Order
from products.models import Product


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    orders = Order.objects.all()
    ctx = {
        'products': products,
        'categories': categories,
        'orders': orders,
    }
    return render(request, 'dashboard/index.html', ctx)