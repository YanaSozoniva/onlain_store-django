from django.contrib import admin
from catalog.models import Category, Product, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели категория"""
    list_display = ('id', 'name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели товара"""
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description', )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Класс для настройки отображения модели контакты"""
    list_display = ('id', 'country', 'address', 'individual_tax_index')
    list_filter = ('country',)
    search_fields = ('country', 'individual_tax_index',)
