from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()
