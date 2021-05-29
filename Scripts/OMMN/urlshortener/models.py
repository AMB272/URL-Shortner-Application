from django.db import models

from .utils import Code_generator, create_shortcode

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
    shortcode = models.CharField(max_length=15, unique=True, blank=True,default='defcode')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    objects = OMMNUrlManager()

    def save(self, *args, **kwargs):
        #print("something")
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(OMMNUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
