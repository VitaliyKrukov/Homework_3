from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from catalog.models import Product


class HomeTempView(TemplateView):
    template_name = "cars/home.html"


class ContactsTempView(TemplateView):
    template_name = "cars/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(CreateView):
    model = Product
    fields = [
        "name",
        "description",
        "image_url",
        "category",
        "purchase_price",
        "created_at",
        "updated_at",
    ]
    success_url = reverse_lazy("cars:products_list")


class ProductUpdateView(UpdateView):
    model = Product
    fields = [
        "name",
        "description",
        "image_url",
        "category",
        "purchase_price",
        "created_at",
        "updated_at",
    ]
    success_url = reverse_lazy("cars:products_list")

    def get_success_url(self):
        return reverse("cars:products_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("cars:products_list")
