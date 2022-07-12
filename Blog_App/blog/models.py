from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self):
        return self.title
