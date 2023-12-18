
from django.urls import path,include
from .views import *
urlpatterns = [
    
    path('',home,name='home'),
    path('delete/<int:roll>',delete_data,name = 'dlt')
]
