from django.forms import ModelForm
from django.core.exceptions import ValidationError
from catalog.models import Product

EXCEPTION_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(ModelForm):
    """Класс для создания формы (добавления нового товара)"""

    class Meta:
        model = Product
        fields = ["name", "description", "photo_product", "category", "price"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name.lower() in EXCEPTION_WORDS:
            raise ValidationError(f'Вы ввели запрещенное слово {name}! Исправляйтесь!!!')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')

        for word in EXCEPTION_WORDS:
            if word in description.lower():
                raise ValidationError(f'Вы ввели запрещенное слово {word}! Исправляйтесь!!!')
            return description
