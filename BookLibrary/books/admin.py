from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Book)
admin.site.register(UserModel)
admin.site.register(BorrowedBook)
admin.site.register(BookReview)