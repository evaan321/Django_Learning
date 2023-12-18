from django import forms

from .models import *

class profileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'