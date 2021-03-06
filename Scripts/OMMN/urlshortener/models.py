from OMMN.settings import SHORTCODE_MAX
from django.db import models
from django.conf import settings
from django_hosts.resolvers import reverse

from .utils import Code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class OMMNUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(OMMNUrlManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        qs = OMMNUrl.objects.filter(id__gte=1) #id greater than or equal to 1
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes += 1
        return f"New codes generated: {new_codes}"

# Create your models here.
class OMMNUrl(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    objects = OMMNUrlManager()

    def save(self, *args, **kwargs):
        #print("something")
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not "http" in self.url:
            self.url = 'http://' + self.url
        super(OMMNUrl, self).save(*args, **kwargs)

    def get_short_url(self):
        #url_path = reverse("scode", kwargs={'shortcode':self.shortcode}, host='ommn-url', scheme='http')
        url_path = f"http://ommn-url.herokuapp.com/{self.shortcode}"
        return url_path

    def __str__(self):
        return str(self.url)
