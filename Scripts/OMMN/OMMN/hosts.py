from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    #host(r'www', settings.ROOT_URLCONF, name='ommn-url'),
    host(r'(?!www).*', 'OMMN.hostsconf.urls', name='wildcard'),
)