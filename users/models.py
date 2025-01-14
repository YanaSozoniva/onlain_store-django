from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35, verbose_name="Телефон", null=True, blank=True, help_text="Введите номер телефона"
    )
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="Аватар", null=True, blank=True, help_text="Загрузите свой аватар"
    )
    country = models.CharField(max_length=35, verbose_name="Страна", blank=True, null=True, help_text="Укажите страну")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
