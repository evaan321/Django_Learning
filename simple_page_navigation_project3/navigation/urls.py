from django.urls import path,include
from .views import contact,about
urlpatterns = [

    path('contact/',contact),
    path('about/',about)
    
    
]
