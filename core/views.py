from django.shortcuts import render, redirect
from .forms import NewsLetterForm
from .models import SiteSettings, ContactUs


def home(request):
    return render(request, 'core/home.html', {})


def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect("core:home")


def contactus(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if firstname and lastname and email and phone_number and subject and message != "":
            ContactUs.objects.create(firstname=firstname, lastname=lastname, email=email, phone_number=phone_number, subject=subject, message=message)
        else:
            print('parameters is none')
    sitesettings = SiteSettings.objects.all().last
    return render(request, 'core/contact.html', {"sitesettings":sitesettings})