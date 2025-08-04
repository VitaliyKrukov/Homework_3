from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, product_details, products_list

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products_list", products_list, name="products_list"),
    path("products/<int:pk>/", product_details, name="product_details"),
]
