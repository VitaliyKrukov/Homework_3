from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product


class HomeTempView(TemplateView):
    template_name = "catalog/home.html"


class ContactsTempView(TemplateView):
    template_name = "catalog/contacts.html"


class ProductListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            self.object.views_counter += 1
            self.object.save()
            return self.object
        raise PermissionDenied


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_success_url(self):
        return reverse("catalog:products_detail", args=[self.kwargs.get("pk")])

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data.get("formset")

        if formset is None:
            self.object = form.save()
            return super().form_valid(form)

        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(
                self.get_context_data(form=form, formset=formset)
            )

    def get_form_class(self):
        user = self.request.user
        self.object = self.get_object()  # Получаем объект продукта

        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product") and user.has_perm(
            "catalog.can_change_publish_status"
        ):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")
