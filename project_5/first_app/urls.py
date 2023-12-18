from django.urls import path
from .views import *

urlpatterns = [
   
    path('',index,name='home'),

    path('about/<int:id>',about,name = 'about')
]
