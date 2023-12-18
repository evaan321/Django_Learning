from django.shortcuts import render,redirect
from .forms import profileForm
# Create your views here.

def add_profile(request):
    if request.method == 'POST':

        form = profileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_profile')
    else:
        form =profileForm()
    return render(request,'add_profile.html',{"form":form})