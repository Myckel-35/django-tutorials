from django.shortcuts import render

# Create your views here.
def page(req):
    return render(req, 'en/public/index.html')
