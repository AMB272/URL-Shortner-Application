from typing import ContextManager
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

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
        context = {
            "title": "Submitted URL",
            "form": form
        }
        template = "urlshortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = OMMNUrl.objects.get_or_create(url=new_url)
            context = {
                "object":obj,
                "created":created,
            }
            if created:
                template = "urlshortener/success.html"
            else:
                template = "urlshortener/already-exists.html"

        return render(request, template, context)

# Create your views here.
# def ommn_redirect_view(request, shortcode=None, *args, **kwargs): #function based view
#     obj = get_object_or_404(OMMNUrl, shortcode=shortcode)
#     return HttpResponseRedirect(obj.url)

class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs): #class based view
        obj = get_object_or_404(OMMNUrl, shortcode=shortcode)
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)