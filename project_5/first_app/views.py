from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , 'index.html')

def about(request,id):
    return render(request , 'index.html',{'id':id})