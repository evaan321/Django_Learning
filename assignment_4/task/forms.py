from django import forms



from .models import *


class taskForm(forms.ModelForm):

    class Meta:
        model = TaskModel
        fields = ['taskTitle','taskDetail','assign','category']

        widgets = {'assign':forms.DateTimeInput(attrs={'type':'datetime-local'})}
        
        
    
