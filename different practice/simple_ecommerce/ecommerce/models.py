from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 200)
    price = models.IntegerField()
    desc = models.TextField()
    category = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='products/')
    def __str__(self) -> str:
        return self.title