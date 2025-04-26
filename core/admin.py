from django.contrib import admin
from .models import SiteSettings, Newsletter, ContactUs


admin.site.register(SiteSettings)
admin.site.register(Newsletter)
admin.site.register(ContactUs)