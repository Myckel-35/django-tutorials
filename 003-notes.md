[Index](README.md)
[Back](002-notes.md)
[Next](004-notes.md)

# Notes for Chapter 3

Ziel: First Website to show Hello World.

Urls defined in [`djale/urls.py`](djale/urls.py)

```python3
# a line in settings.py
ROOT_URLCONF = 'djale.urls'
```

## To understan URLs we need to learn some regexp stuff.

in the book are only some syntaxes

```
tests{0,} == tests*
tests{1,} == tests+
tests{2} matches only testss
tests{2,} matches tess and testsss ...
```

## Lets get started

The development (built in) server from django is not for production use.

```bash
# start the development webserver
python3 manage.py runserver 127.0.0.1:8000
# or only
python3 manage.py runserver
```

## create our hello world site

[`djale/urls.py`](djale/urls.py)
```python3
...
import TasksManager.views.index

urlpatterns = [
    ...
    url(r'^$', TasksManager.views.index.page),
    url(r'^index$', TasksManager.views.index.page),
]
```

[`TasksManager/views/index.py`](TasksManager/views/index.py)
```python3
from django.http import HttpResponse

def page(req):
    return HttpResponse("Hallo Welt")
```

