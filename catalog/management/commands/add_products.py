from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add test Product to the database"

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(
            name="Овощи", description="Краснодарские овощи"
        )

        products = [
            {
                "name": "Огурец",
                "description": "Иванов",
                "purchase_price": 20,
                "category": category,
            },
            {
                "name": "Помидор",
                "description": "Петров",
                "purchase_price": 20,
                "category": category,
            },
        ]

        for products_data in products:
            products, created = Product.objects.get_or_create(**products_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added products: {products.name} {products.description}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Student already exists: {products.name} {products.description}"
                    )
                )
