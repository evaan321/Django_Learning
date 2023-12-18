from django.shortcuts import render,redirect
from .forms import CategoryForm
# Create your views here.

def add_Category(request):
    if request.method == 'POST':

        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_Category')
    else:
        form =CategoryForm()
    return render(request,'category.html',{"form":form})