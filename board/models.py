from django.db import models
from accounts.models import User


class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
