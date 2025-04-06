from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'حساب کاربری شما ایجاد شد{username}')
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    return render(request,'accounts/register.html',{'form':form})





    