from django import forms
from categories.models import Category
from django.core.exceptions import ValidationError



class ProductForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
        'placeholder': 'Enter Product Name'
    }))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
        }),
        empty_label="Select Category"
    )
    price = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
        'rows': '3'
    }))
    image = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'mt-1 block w-full',
    }))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError("Mahsulot nomi talab qilinadi.")
        if len(name) < 3:
            raise ValidationError("Mahsulot nomi kamida 3 ta belgi bo'lishi kerak.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        try:
            price = float(price)
            if price <= 0:
                raise ValidationError("Narx musbat raqam bo'lishi kerak.")
        except ValueError:
            raise ValidationError("Narx noto'g'ri kiritildi. Faqat raqam bo'lishi kerak.")
        return price

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 10:
            raise ValidationError("Tavsif kamida 10 ta belgidan iborat bo'lishi kerak.")
        return description

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if not image.name.endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError("Faqat PNG, JPG va JPEG rasm formatlari ruxsat etiladi.")
        return image