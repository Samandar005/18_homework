from django.db import models
from categories.models import Category
from django.utils.text import slugify
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('products:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_update_url(self):
        return reverse('products:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('products:delete', args=[self.pk])

    def __str__(self):
        return f"{self.name}"


