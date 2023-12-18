from django.shortcuts import render,redirect

from .models import *
# Create your views here.

from category.models import TaskCategory

from .forms import taskForm

def addTask(request):
   
   if request.method == 'POST':
      form = taskForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect ('addTask')
   else:
      form =taskForm()
   return render(request,'addTask.html',{'form':form})

def showTask(request):

   data = TaskModel.objects.all()

   categoryData = TaskCategory.objects.all()

   return render (request,'ShowTask.html',{'data':data})


def edit(request,id):
   task = TaskModel.objects.get(pk=id)

   form = taskForm(instance=task)


   if request.method == 'POST':
      form = taskForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect ('showTask')
   
   return render(request,'addTask.html',{'form':form})

def delete(request,id):
   task = TaskModel.objects.get(pk=id)

   task.delete()
   return redirect('showTask')