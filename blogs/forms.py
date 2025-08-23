from django.forms import ModelForm

from blogs.models import Blogs


class BlogsForm(ModelForm):
    class Meta:
        model = Blogs
        exclude = ("views_counter",)
