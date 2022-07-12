from django.views.generic import ListView, DetailView

from .models import Post


class PostList(ListView):
    model = Post
    template_name = "posts/post_list.html"


class PostDetail(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
