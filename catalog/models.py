from django.db import models


class Category(models.Model):
    """Класс для создания модели(таблицы) Категория"""

    name = models.CharField(max_length=50, verbose_name="Категория", help_text="Введите название категории")
    description = models.TextField(
        verbose_name="Описание категории", help_text="Введите описание категории", blank=True, null=True
    )

    def __str__(self):
        """Метод для строкового отображения информации о категории"""
        return self.name

    class Meta:
        """Данный класс используется для добавления метаданных к модели:
        наименование модели в единственном и множественном числе"""

        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    """Класс для создания модели(таблицы) Продукции"""

    name = models.CharField(max_length=50, verbose_name="Товар", help_text="Введите название товара")
    description = models.TextField(
        verbose_name="Описание товара", help_text="Введите описание товара", blank=True, null=True
    )
    photo_product = models.ImageField(upload_to="photos/", verbose_name="Изображение", blank=True, null=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена", help_text="Укажите цену за покупку товара", default=0
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Введите категорию товара",
        blank=True,
        null=True,
        related_name="products",
    )
    created_at = models.DateField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Дата последнего изменения", auto_now=True)

    def __str__(self):
        """Метод для строкового отображения информации о продукте"""
        return f"{self.name}, относится к категории {self.category}, цена: {self.price}"

    class Meta:
        """Данный класс используется для добавления метаданных к модели:
        наименование модели в единственном и множественном числе,
        а также порядок сортировки продукции при выборке из БД"""

        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name', 'category', 'price']


class Contact(models.Model):
    """Класс для создания модели(таблицы) контакты"""

    country = models.CharField(max_length=50, verbose_name="Страна", help_text="Введите название страны")
    address = models.CharField(max_length=150, verbose_name="Адрес", help_text="Введите Ваш адрес", blank=True, null=True)
    individual_tax_index = models.IntegerField(verbose_name='ИНН', blank=True, null=True)

    def __str__(self):
        """Метод для строкового отображения информации о контактах"""
        return f'{self.country}, {self.address}'

    class Meta:
        """Данный класс используется для добавления метаданных к модели:
        наименование модели в единственном и множественном числе"""

        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
