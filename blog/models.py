from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(unique=True, max_length=100, allow_unicode=True, verbose_name='نامک')
    created = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True,  verbose_name="عنوان تگ")
    slug = models.SlugField(unique=True, max_length=100, allow_unicode=True, verbose_name='نامک')
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

    def __str__(self):
        return self.title
