from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['balance', 'userReview']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)


class DepositForm(forms.Form):
    amount = forms.IntegerField(min_value=1)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['review_text']
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 5}),
        }