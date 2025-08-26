from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (ContactsTempView, HomeTempView, ProductCreateView,
                           ProductDeleteView, ProductDetailView,
                           ProductListView, ProductUpdateView)

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", HomeTempView.as_view(), name="home"),
    path("contacts/", ContactsTempView.as_view(), name="contacts"),
    path("product_list/", ProductListView.as_view(), name="products_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
]
