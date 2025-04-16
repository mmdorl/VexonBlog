from core.models import Newsletter, SiteSettings
from core.forms import NewsLetterForm



def blog_func(request):
    site_settings = SiteSettings.objects.all().last()
    return {'site_settings': site_settings}