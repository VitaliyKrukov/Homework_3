from django.db import models


class Brand(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Марка автомобиля",
        help_text="Введите марку автомобиля",
    )
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание автомобиля",
        help_text="Введите описание автомобиля",
    )
    image_url = models.ImageField(
        upload_to="product/image",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение автомобиля",
    )
    creation_date = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Введите дату создания",
    )
    publication_flag = models.IntegerField(null=True, blank=True)

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0,
    )

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
        ordering = ["creation_date", "title"]

    def __str__(self):
        return f"{self.title}, {self.publication_flag}, {self.creation_date}"
