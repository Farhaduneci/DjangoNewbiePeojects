from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "blog/home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "blog/new_post.html"
    fields = ["author", "title", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog/edit_post.html"
    fields = ["author", "title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"

    def get_success_url(self):
        return reverse("home")
