from typing import ContextManager
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import OMMNUrl

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Submit URL",
            "form": the_form
        }
        return render(request, "urlshortener/home.html", context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        # print(request.POST.get("url"))
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        context = {
            "title": "Submitted URL",
            "form": form
        }
        return render(request, "urlshortener/home.html", context)

# Create your views here.
# def ommn_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
#     obj = get_object_or_404(OMMNUrl, shortcode=shortcode)
#     return HttpResponseRedirect(obj.url)

class OmmnCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs): #class based view
        obj = get_object_or_404(OMMNUrl, shortcode=shortcode)
        return HttpResponse(f"hello again {shortcode}")