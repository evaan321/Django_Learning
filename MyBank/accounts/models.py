from django.db import models
from django.contrib.auth.models import User
# Create your models here.


ACCOUNT_TYPE = [
    ('Savings','Savings'),
    ('Current','Current'),
]
GENDER = [
    ('Male','Male'),
    ('Female','Female'),
]

class UserBankAccount(models.Model):
    
    user = models.OneToOneField(User, on_delete = models.CASCADE,related_name='account')

    ac_type = models.CharField(max_length=10,choices = ACCOUNT_TYPE)

    ac_number = models.IntegerField(unique= True)

    birth_date = models.DateField (null= True , blank = True)

    gender =  models.CharField(max_length=10,choices = GENDER)

    first_deposit_date = models.DateField(auto_now_add=True)

    balance = models.DecimalField(default = 0 , max_digits = 12 , decimal_places=2)

    def __str__(self) -> str:
        return str(self.ac_number)

class UserAddress(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='address')

    street = models.CharField(max_length = 100)

    city = models.CharField(max_length=20)

    postal_code = models.IntegerField()

    country = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return str(self.user.email)
