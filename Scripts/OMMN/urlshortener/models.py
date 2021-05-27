from django.db import models
import random, string

def Code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

# Create your models here.
class OMMNUrl(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        #print("something")
        self.shortcode = Code_generator()
        super(OMMNUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
