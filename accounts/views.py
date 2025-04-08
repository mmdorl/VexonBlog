from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'حساب کاربری شما ایجاد شد{username}') 
            login(request,user)
            return redirect("/")
            
    else:
        form = RegisterForm()
    return render(request,'accounts/register.html',{'form':form})



def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('/')

    
    if request.method == "POST":
        
        form = LoginForm(request.POST)
        if form.is_valid():
            
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get("password")
            user = User.objects.get(username=form.cleaned_data.get('username'))
            
            login(request,user)
            return redirect("/")
        
    else:
        form = LoginForm()
    return render(request,"accounts/login.html",{'form':form})


def user_logout(request):
    logout(request)
    return redirect("/")



    