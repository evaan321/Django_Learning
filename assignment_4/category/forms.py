from django import forms

from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'
        
        
        
