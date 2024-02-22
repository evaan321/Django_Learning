from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

ACCOUNT_TYPE = [
    ('Savings','Savings'),
    ('Current','Current'),
]
GENDER = [
    ('Male','Male'),
    ('Female','Female'),
]
class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER)
    ac_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    street = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'ac_type', 'birth_date','gender', 'postal_code', 'city','country', 'street']
        
        # form.save()
    def save(self, commit=True):
        our_user = super().save(commit=False) # ami database e data save korbo na ekhn
        if commit == True:
            our_user.save() # user model e data save korlam
            ac_type = self.cleaned_data.get('account_type')
            gender = self.cleaned_data.get('gender')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
            birth_date = self.cleaned_data.get('birth_date')
            city = self.cleaned_data.get('city')
            street = self.cleaned_data.get('street')
            
            UserAddress.objects.create(
                user = our_user,
                postal_code = postal_code,
                country = country,
                city = city,
                street = street
            )
            UserBankAccount.objects.create(
                user = our_user,
                ac_type  = ac_type,
                gender = gender,
                birth_date =birth_date,
                ac_no = 100000+ our_user.id
            )
        return our_user