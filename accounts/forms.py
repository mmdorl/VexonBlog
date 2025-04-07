from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ValidationError

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']

        

class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    



       