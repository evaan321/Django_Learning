from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    myproducts = Product.objects.all()

    return render(request,'index.html', {'product' : myproducts})

def detail(request,id):
    myproduct = Product.objects.get(id= id)

    return render(request ,'detail.html', {'p': myproduct})

