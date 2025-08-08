from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    image_url = models.ImageField(
        upload_to="product/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="catalog",
    )
    purchase_price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата модификации",
        help_text="Введите дату модификации",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["created_at", "name"]

    def __str__(self):
        return f"{self.name}, {self.purchase_price}, {self.created_at}"


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
