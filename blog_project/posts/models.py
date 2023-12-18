from django.db import models

from categories.models import *

from author.models import *
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    category = models.ManyToManyField(Category)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title