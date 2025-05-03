from django.contrib import admin
from . import models
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(models.Category)
class CategoryAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'get_created_jalali']
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a، %d %b %Y')


@admin.register(models.Tag)
class TagAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'get_created_jalali']
    prepopulated_fields = {'slug': ('title',)}

    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a، %d %b %Y')
