from django import forms
from catalog.models import Product


class AddProduct(forms.ModelForm):
    """Класс для создания формы (добавления нового товара)"""
    class Meta:
        model = Product
        fields = ['name', 'description', 'photo_product', 'category', 'price']
