from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView,CreateView
from django.contrib.auth.views import LoginView,LogoutView
from .models import CarModel,Brand,Comment,UserModel
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib import messages
from django.contrib.auth.models import User 

class HomeView(TemplateView):
    template_name = 'Home.html'
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["data"] = CarModel.objects.all()
        context['count']= CarModel.objects.all().count()
        context['brand']= Brand.objects.all()
        return context

def filterView(request,brand_slug = None):
    data = CarModel.objects.all()

    if brand_slug is not None:
        filterCar = Brand.objects.get(BrandName = brand_slug)
        data = CarModel.objects.filter(brand = filterCar)
        count = CarModel.objects.filter(brand = filterCar).count() 
    return render(request,'Home.html',{'data':data,'count':count})

class DetailView(DetailView):
    template_name= 'detail.html'
    
    model = CarModel

    context_object_name= 'data'

    # def comment(self):
    #     comment_form = CommentForm(data=self.request.POST)
    #     if comment_form.is_valid():
    #         new_comment = comment_form.save()
    #     else:
    #         comment_form=CommentForm()  
    #     return comment_form 
       
        
    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context['form']= DetailView.comment(self)
    #     # context['comment']= Comment.objects.filter(pk = CarModel.pk)

        


def register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            
            return redirect ('Home')
        
    else:
        register_form = RegistrationForm()
    return render(request,'register.html',{'form':register_form})

class LoginUserView(LoginView):
    template_name = 'register.html'
    form_class = AuthenticationForm
    
    def get_success_url(self) -> str:
        return reverse_lazy('Home')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ChangeUserData(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('edit')
    
    else:
        profile_form = ChangeUserData(instance = request.user)

    return render(request, 'change.html', {'form' : profile_form})
    

class Logout(LogoutView):
   def get_success_url(self):
       return reverse_lazy('Home')
    
    

def profile(request):

    data = UserModel.objects.get(user = request.user)
    
    
    return render(request,'profile.html',{'data':data})


def buyCar(request,id):
    try:
       
        user = UserModel.objects.get(user=request.user)
    except UserModel.DoesNotExist:
        user = UserModel.objects.create(user=request.user)
    car = CarModel.objects.get(pk = id)
    
    if car.quantity > 0:
        car.quantity = car.quantity - 1
        car.save()
        user.car.add( car)
        user.save()
    else:
        messages.error(request,'This car is not available')

    return redirect('detail',pk=car.pk)


        

  