from django.db import models

# Create your models here.


class Student(models.Model):
    roll = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=20)

    address = models.CharField(max_length=50,default='Uttara')

    motherName = models.CharField(max_length=20,default='rokeya begum')