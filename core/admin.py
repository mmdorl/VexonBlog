from django.contrib import admin
from .models import SiteSettings, Newsletter


admin.site.register(SiteSettings)
admin.site.register(Newsletter)
