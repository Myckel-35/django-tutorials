from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page(req):
    return HttpResponse("Hallo Welt")
