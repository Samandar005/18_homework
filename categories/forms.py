from django import forms
from django.core.exceptions import ValidationError


class CategoryForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
        'placeholder': 'Enter Category Name',
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'mt-1 block w-full border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
        'placeholder': 'Enter description',
        'rows': '3',
    }))
    icons = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'mt-1 block w-full',
    }))

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError("Kategoriyaning nomi talab qilinadi.")
        if len(name) <= 2:
            raise ValidationError("Kategoriyaning nomi aynan 2 ta belgi bo'lishi kerak.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not description:
            raise ValidationError("Tavsif talab qilinadi.")
        if len(description) <= 10:
            raise ValidationError("Tavsif kamida 10 ta belgidan iborat bo'lishi kerak.")
        return description

    def clean_icons(self):
        icon = self.cleaned_data.get('icons')
        if icon:
            if not icon.name.endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError("Faqat PNG, JPG, va JPEG rasmlari ruxsat etiladi.")
        return icon