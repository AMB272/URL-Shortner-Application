from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

# Create your views here.
def ommn_redirect_view(request, *args, **kwargs): #function based view
    return HttpResponse("hello")

class OmmnCBView(View):
    def get(self, request, *args, **kwargs): #class based view
        return HttpResponse("hello again")