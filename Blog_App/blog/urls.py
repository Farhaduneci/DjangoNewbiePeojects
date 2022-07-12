from django.urls import path

from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("posts/new/", BlogCreateView.as_view(), name="new_post"),
    path("posts/<int:pk>/edit/", BlogUpdateView.as_view(), name="edit_post"),
    path("posts/<int:pk>/delete/", BlogDeleteView.as_view(), name="delete_post"),
]
