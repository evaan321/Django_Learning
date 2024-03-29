from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from django.views.generic import FormView
from django.contrib.auth import login
# Create your views here.


class UserRegistrationView(FormView):
    template_name = ''
    form_class = UserRegistrationForm
    success_url = ''

    def form_valid(self, form):
        user = form.save()
        login(user)
        return super().form_valid(form)
