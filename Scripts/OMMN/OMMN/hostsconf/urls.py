from django.contrib import admin
from django.urls import path

from .views import wildcard_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wildcard_redirect),
    path('<slug:shortcode>/', wildcard_redirect),
]
