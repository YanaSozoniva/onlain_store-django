from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_products_by_category(category_id):
    """Функция получения списка продуктов по выбранной категории из кеша, если кэш пустой - из бд"""
    return Product.objects.filter(category=category_id)
