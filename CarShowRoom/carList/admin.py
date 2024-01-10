from django.contrib import admin

from .models import CarModel,Brand,Comment,UserModel
# Register your models here.

admin.site.register(CarModel)

admin.site.register(Brand)

admin.site.register(Comment)
admin.site.register(UserModel)