# Create your models here.
from auth.models import User
from content.models import Book
from django.db import models


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    content = models.CharField(max_length=120)

    def __str__(self):
        return self.user.username
