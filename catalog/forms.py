from django.forms import ModelForm
from catalog.models import Product


class ProductForm(ModelForm):
    """Класс для создания формы (добавления нового товара)"""

    class Meta:
        model = Product
        fields = ["name", "description", "photo_product", "category", "price"]
