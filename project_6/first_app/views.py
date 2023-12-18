from django.shortcuts import render
from . forms import contactForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        name  = request.POST.get('username')
        email = request.POST.get('email')
        return render(request,'index.html',{'name':name,'email':email})

    return render(request,'index.html')


def contact_form(request):
    if request.method == 'POST':

        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open ('./first_app/upload/'+ file.name,'wb+') as dest:
                for chunk in file.chunks():
                    dest.write(chunk)
            data = form.cleaned_data
            return render(request,'django-form.html',{'form':form,'data':data})
    else:
         form = contactForm()
    
    return render(request,'django-form.html',{'form':form})




