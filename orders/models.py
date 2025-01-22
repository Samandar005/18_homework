from django.db import models
from django.urls import reverse
from products.models import  Product


class Order(models.Model):
    STATUS_CHOICES = [
        ('pd', 'Pending'),
        ('pg', 'Processing'),
        ('shd', 'Shipped'),
        ('dd', 'Delivered'),
        ('cd', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=200)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES,)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def get_detail_url(self):
        return reverse('orders:detail', args=[self.pk])


    def get_total_price(self):
        total = sum(item.quantity * item.product.price for item in self.order_items.all())
        return total

    def __str__(self):
        return f"{self.customer_name}"


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')

