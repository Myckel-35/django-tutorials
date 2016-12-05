from django.shortcuts import render

def page(req):
    return render(req, 'en/public/connection.html')
