from django.db import models

from django.contrib.auth.models import User
# Create your models here.







class Brand(models.Model):

    BrandName = models.CharField(max_length=20)
    
    


    def __str__(self) -> str:
        return self.BrandName
    



class CarModel(models.Model):

    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    title = models.CharField(max_length=20)
    desc = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    
    
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    car  = models.ForeignKey(CarModel,on_delete= models.CASCADE,null=True,blank= True)

class UserModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True, blank = True)
    car  = models.ManyToManyField('CarModel',blank=True)
    