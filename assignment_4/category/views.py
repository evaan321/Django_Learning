from django.shortcuts import render,redirect

# Create your views here.

from .forms import *

def addCategory(request):
   
   if request.method == 'POST':
      form = CategoryForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect ('addTask')
   else:
      form =CategoryForm()
   return render(request,'add_category.html',{'form':form})