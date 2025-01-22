from django import forms
from .models import Order, OrderItem

class OrderUpdateForm(forms.Form):
    order_status = forms.ChoiceField(choices=Order.STATUS_CHOICES, widget=forms.Select(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}))
    customer_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}))
    customer_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}))
    customer_phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}))
    customer_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm'}))

class OrderItemUpdateForm(forms.Form):
    product_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'w-full border-gray-300 rounded-md shadow-sm'}))
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'w-full border-gray-300 rounded-md shadow-sm'}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'w-full border-gray-300 rounded-md shadow-sm'}))
