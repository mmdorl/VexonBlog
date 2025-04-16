from django.shortcuts import render, redirect
from .forms import NewsLetterForm



def home(request):
    return render(request, 'core/home.html', {})


def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("core:home")
