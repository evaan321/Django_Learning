from django.db import models
from django.contrib.auth.models import User
CATEGORY  = [
    ('Horror','Horror'),
    ('Fiction','Fiction'),
    ('Novel','Novel'),
    ('Fantasy','Fantasy'),
    ('Story','Story')
]

class Book(models.Model):
    title = models.CharField(max_length = 20)
    desc = models.TextField()
    image = models.ImageField(upload_to='uploads')
    bPrice = models.IntegerField()
    category = models.CharField(max_length = 15,choices=CATEGORY)
    userReview  = models.TextField(blank = True,null = True)

    def __str__(self) -> str:
        return self.title

class UserModel (models.Model):
   user = models.OneToOneField(User, related_name='myUser', on_delete=models.CASCADE) 

   balance = models.IntegerField(default = 0)
   userReview = models.ForeignKey(Book,on_delete= models.CASCADE,blank = True,null = True ,default  = None)
   
class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank = True,null = True )
    book = models.ForeignKey(Book, on_delete=models.CASCADE,blank = True,null = True )
    review_text = models.TextField()

class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank = True,null = True )
    book = models.ForeignKey(Book, on_delete=models.CASCADE,blank = True,null = True )
    borrowed_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(null=True, blank=True)
    returned = models.BooleanField(default=False) 




