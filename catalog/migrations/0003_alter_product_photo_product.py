# Generated by Django 5.1.3 on 2025-01-07 15:25

import catalog.validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="photo_product",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="photos/",
                validators=[catalog.validator.FileSizeValidator(), catalog.validator.ImageFormatValidator()],
                verbose_name="Изображение",
            ),
        ),
    ]
