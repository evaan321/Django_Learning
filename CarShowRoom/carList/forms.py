from django.forms import ModelForm
from .models import Comment,CarModel
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User 

class CommentForm(ModelForm):
    
    class Meta:
        model = Comment
        fields = '__all__'


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']