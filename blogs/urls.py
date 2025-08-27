from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import (
    BlogsCreateView,
    BlogsDeleteView,
    BlogsDetailView,
    BlogsListView,
    BlogsUpdateView,
)

app_name = BlogsConfig.name

urlpatterns = [
    path("blog_list/", BlogsListView.as_view(), name="blog_list"),
    path("blog/<int:pk>/", BlogsDetailView.as_view(), name="blog_details"),
    path("blog/create/", BlogsCreateView.as_view(), name="blog_create"),
    path("blog/<int:pk>/update/", BlogsUpdateView.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", BlogsDeleteView.as_view(), name="blog_delete"),
]
