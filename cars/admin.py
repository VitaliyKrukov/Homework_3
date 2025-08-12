from django.contrib import admin

from cars.models import Brand


@admin.register(Brand)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
    )
    search_fields = ("title", "content")
