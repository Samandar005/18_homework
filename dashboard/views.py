from django.shortcuts import render
from categories.models import Category
from orders.models import Order
from products.models import Product
from django.db.models import Sum


def home(request):
    total_price = Product.objects.aggregate(Sum('price'))['price__sum']
    total_categories = Category.objects.count()
    total_orders = Order.objects.annotate(total_quantity=Sum('order_items__quantity')).aggregate(total=Sum('total_quantity'))[
        'total']

    recent_products = Product.objects.all().order_by('-created_at')[:9]

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
        'total_price': total_price,
        'total_categories': total_categories,
        'total_orders': total_orders,
        'recent_products': recent_products,
    }
    return render(request, 'dashboard/index.html', ctx)