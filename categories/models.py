from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    icons = models.FileField(upload_to='categories/', null=True, blank=True,)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('categories:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def get_update_url(self):
        return reverse('categories:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('categories:delete', args=[self.pk])

    def __str__(self):
        return f"{self.name}"
