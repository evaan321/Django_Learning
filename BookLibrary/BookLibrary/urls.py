"""
URL configuration for BookLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from books.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', CustomRegisterView.as_view(), name='register'), 
    path('', HomeView.as_view(), name='home'),
    path('book-detail/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('category/<str:category>/', CategoryView.as_view(), name='category-list'),
    path('deposit/', deposit_money, name='deposit-money'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow-book'),
    path('profile/', profile, name='profile'),
    path('review/<int:book_id>/', review_book, name='review-book'),
    path('return/<int:borrowed_book_id>/', return_book, name='return-book'),
    path('logout/', custom_logout, name='logout'),

]
urlpatterns += static(settings.MEDIA_URL ,document_root = settings.MEDIA_ROOT)
