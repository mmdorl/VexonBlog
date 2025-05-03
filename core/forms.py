from django import forms
from .models import Newsletter, SiteSettings, ContactUs


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email', )


# class ContactUsForm(forms.ModelForm):
#     class Meta:
#         model = ContactUs
#         fields = ['firstname', 'lastname', 'email', 'phone_number','subject','message']
#         label = ['نام', 'نام خانوادگی', 'ایمیل', 'شماره تلفن', 'موضوع', 'پیام']