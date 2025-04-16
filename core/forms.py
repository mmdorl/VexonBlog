from django import forms
from .models import Newsletter, SiteSettings


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email', )


