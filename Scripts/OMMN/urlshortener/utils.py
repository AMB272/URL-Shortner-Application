import random, string, sys

from django.conf import settings

SHORTCODE_MIN = getattr(settings, "SHORTCODE_MIN", 6)

def Code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
    new_code = Code_generator(size=size)
    klass = instance.__class__
    qs_exists = klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code