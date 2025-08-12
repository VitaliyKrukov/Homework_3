from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from cars.models import Brand


class BrandListView(ListView):
    model = Brand

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(publication_flag=True)
            .order_by("-creation_date")
        )


class BrandDetailView(DetailView):
    model = Brand

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BrandCreateView(CreateView):
    model = Brand
    fields = [
        "title",
        "content",
        "image_url",
        "creation_date",
        "publication_flag",
        "views_counter",
    ]
    success_url = reverse_lazy("cars:brand_list")


class BrandUpdateView(UpdateView):
    model = Brand
    fields = [
        "title",
        "content",
        "image_url",
        "creation_date",
        "publication_flag",
        "views_counter",
    ]
    success_url = reverse_lazy("cars:brand_list")

    def get_success_url(self):
        return reverse("cars:brand_detail", args=[self.kwargs.get("pk")])


class BrandDeleteView(DeleteView):
    model = Brand
    success_url = reverse_lazy("cars:brand_list")
