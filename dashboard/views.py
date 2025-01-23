from django.shortcuts import render
from categories.models import Category
from orders.models import Order
from products.models import Product


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    orders = Order.objects.all()
    category_names = [category.name for category in Category.objects.all()]
    category_product_counts = [category.products.count() for category in Category.objects.all()]
    ctx = {
        'products': products,
        'categories': categories,
        'orders': orders,
        'category_names': category_names,
        'category_product_counts': category_product_counts,
    }
    return render(request, 'dashboard/index.html', ctx)