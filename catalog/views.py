from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    return render(request, "contacts.html")


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'image_url', 'category', 'purchase_price', 'created_at', 'updated_at']
    success_url = reverse_lazy('catalog:products_list')
