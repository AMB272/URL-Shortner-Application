from django.db import models

from .utils import Code_generator, create_shortcode

# Create your models here.
class OMMNUrl(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True,default='defcode')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        #print("something")
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(OMMNUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
