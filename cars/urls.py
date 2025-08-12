from django.urls import path

from cars.apps import CarsConfig
from cars.views import (
    BrandCreateView,
    BrandDeleteView,
    BrandDetailView,
    BrandListView,
    BrandUpdateView,
)

app_name = CarsConfig.name

urlpatterns = [
    path("brand_list/", BrandListView.as_view(), name="brand_list"),
    path("brand/<int:pk>/", BrandDetailView.as_view(), name="brand_details"),
    path("brand/create/", BrandCreateView.as_view(), name="brand_create"),
    path("brand/<int:pk>/update/", BrandUpdateView.as_view(), name="brand_update"),
    path("brand/<int:pk>/delete/", BrandDeleteView.as_view(), name="brand_delete"),
]
