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