from django.db import models

# Create your models here.
from urlshortener.models import OMMNUrl

class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, OMMNUrl):
            obj, created = self.get_or_create(ommn_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    ommn_url = models.OneToOneField(OMMNUrl, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return f"{self.count}"

