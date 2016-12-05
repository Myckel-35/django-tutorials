from django.shortcuts import render

# Create your views here.
def page(req):
    vars = {
      'hw': "Hallo Welt :)",
      'my_age': 31,
      'capitals': ["Berlin", "London", "Paris", "Washington"],
      'js_on': "<script>console.log('autoescape on');</script>",
      'js_off': "<script>console.log('autoescape off');</script>"
      }
    return render(req, 'en/public/index.html', vars)
