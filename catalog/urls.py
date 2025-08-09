from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
    contacts,
    home,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("products_list/", ProductListView.as_view(), name="products_list"),
    path("catalog/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
]
