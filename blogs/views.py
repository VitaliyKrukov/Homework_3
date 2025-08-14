from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from blogs.models import Blogs


class BlogsListView(ListView):
    model = Blogs
    template_name = "blogs/blog_list.html"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(publication_flag=True)
            .order_by("-creation_date")
        )


class BlogsDetailView(DetailView):
    model = Blogs
    template_name = "blogs/blog_detail.html"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogsCreateView(CreateView):
    model = Blogs
    template_name = "blogs/blog_form.html"
    fields = [
        "title",
        "content",
        "image_url",
        "creation_date",
        "publication_flag",
        "views_counter",
    ]
    success_url = reverse_lazy("blogs:blog_list")


class BlogsUpdateView(UpdateView):
    model = Blogs
    template_name = "blogs/blog_form.html"
    fields = [
        "title",
        "content",
        "image_url",
        "creation_date",
        "publication_flag",
        "views_counter",
    ]
    success_url = reverse_lazy("blogs:blog_list")

    def get_success_url(self):
        return reverse("blogs:blog_detail", args=[self.kwargs.get("pk")])


class BlogsDeleteView(DeleteView):
    model = Blogs
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy("blogs:blog_list")
