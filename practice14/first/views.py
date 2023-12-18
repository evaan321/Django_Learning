from django.shortcuts import render

from .forms import Form
# Create your views here.

def index(request):
    data = Form()

    return render(request,'index.html',{'form':data})