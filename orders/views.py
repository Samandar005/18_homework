from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .models import Order
from .forms import OrderUpdateForm, OrderItemUpdateForm



def order_list(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    orders = Order.objects.all()

    if search_query:
        orders = orders.filter(customer_name__icontains=search_query)

    if status_filter:
        orders = orders.filter(status=status_filter)

    ctx = {
        'orders': orders,
        'search_query': search_query,
        'status_filter': status_filter,
    }
    return render(request, 'orders/list.html', ctx)

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order_form = OrderUpdateForm(request.POST)
        order_items_forms = [
            (item, OrderItemUpdateForm(request.POST, prefix=f"item_{item.id}"))
            for item in order.order_items.all()
        ]
        if order_form.is_valid() and all(form.is_valid() for _, form in order_items_forms):
            for field in ['order_status', 'customer_name', 'customer_email', 'customer_phone', 'customer_address']:
                setattr(order, field, order_form.cleaned_data[field])
            order.save()

            for item, item_form in order_items_forms:
                item.product.name = item_form.cleaned_data['product_name']
                item.quantity = item_form.cleaned_data['quantity']
                item.product.price = item_form.cleaned_data['price']
                item.save()

            return redirect('orders:detail', pk=order.pk)

    else:
        order_form = OrderUpdateForm(initial={
            'status': order.status,
            'customer_name': order.customer_name,
            'customer_email': order.email,
            'customer_phone': order.phone_number,
            'customer_address': order.address,
        })

        order_items_forms = [
            OrderItemUpdateForm(initial={
                'product_name': item.product.name,
                'quantity': item.quantity,
                'price': item.product.price,
            }, prefix=f"item_{item.id}")
            for item in order.order_items.all()
        ]

    return render(request, 'orders/form.html', {
        'order_form': order_form,
        'order_items_forms': order_items_forms,
        'order': order
    })

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order_items = order.order_items.all()

    for item in order_items:
        item.total_price = item.quantity * item.product.price

    ctx = {
        'order': order,
        'order_items': order_items,
    }
    return render(request, 'orders/detail.html', ctx)