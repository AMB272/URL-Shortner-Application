from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from .models import OMMNUrl

# Create your views here.
def ommn_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
    obj = get_object_or_404(OMMNUrl, shortcode=shortcode)
    # obj_url = None
    # qs = OMMNUrl.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() ==1:
    #     obj = qs.first()
    #     obj_url = obj.url
    return HttpResponseRedirect(obj.url)

class OmmnCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs): #class based view
        obj = get_object_or_404(OMMNUrl, shortcode=shortcode)
        return HttpResponse(f"hello again {shortcode}")