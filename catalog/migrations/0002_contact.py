# Generated by Django 5.1.3 on 2024-12-06 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "country",
                    models.CharField(help_text="Введите название страны", max_length=50, verbose_name="Страна"),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, help_text="Введите Ваш адрес", max_length=150, null=True, verbose_name="Адрес"
                    ),
                ),
                ("individual_tax_index", models.IntegerField(blank=True, null=True, verbose_name="ИНН")),
            ],
            options={
                "verbose_name": "Контакт",
                "verbose_name_plural": "Контакты",
            },
        ),
    ]