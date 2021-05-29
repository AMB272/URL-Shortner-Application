from django.contrib import admin
from django.urls import path

from .views import wildcard_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/<slug:shortcode>/', wildcard_redirect),
    path('b/<slug:shortcode>/', wildcard_redirect),
]
