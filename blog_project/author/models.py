from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.CharField(max_length=100)
    phone_no = models.IntegerField(max_length=11)

    def __str__(self) -> str:
        return self.name