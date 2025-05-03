from django.db import models


class SiteSettings(models.Model):
    Our_team_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='اسم گروه ما')
    about_us_text = models.TextField(null=True, blank=True, verbose_name='متن درباره ما')
    contact_us_text = models.TextField(null=True, blank=True, verbose_name='متن تماس با ما')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='ادرس')
    city_us = models.CharField(max_length=50, null=True, blank=True, verbose_name='شهر')
    phone_us = models.CharField(max_length=20, null=True, blank=True, verbose_name='شماره تماس')
    email_us = models.EmailField(null=True, blank=True, verbose_name='ادرس ایمیل')
    whatsapp_link = models.CharField(max_length=200, null=True, blank=True, verbose_name='لینک واتساپ')
    instagram_link = models.CharField(max_length=200, null=True, blank=True, verbose_name='لینک اینساگرام')
    telegram_link = models.CharField(max_length=200, null=True, blank=True, verbose_name='لینک تلگرام')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.about_us_text


class Newsletter(models.Model):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    date_membership = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')

    class Meta:
        verbose_name = 'عضو خبرنامه'
        verbose_name_plural = 'اعضای خبرنامه'
        
    def __str__(self):
        return self.email
    

class ContactUs(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='نام')
    lastname = models.CharField(max_length=80, verbose_name='نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    phone_number = models.CharField(max_length=11, verbose_name='شماره تلفن')
    subject = models.CharField(max_length=80, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    date_send = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')
    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'
    def __str__(self):
        return f"{self.firstname} {self.lastname}: {self.message[0:50]}"


