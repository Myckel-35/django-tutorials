[Index](README.md)
[Back](003-notes.md)
[Next](#)

# Notes for Chapter 4

Working with templates. YAY

Add a directory as a templates-direcory

[`djale/settings.py`](djale/settings.py)
```python3
TEMPLATES = [
    {
        # ...
        'DIRS': [
            os.path.join(BASE_DIR, 'TasksManager/templates')
            ],
        # ...
    },
]
```

and create the dir

```bash
$ mkdir -p TasksManager/templates/en/public/
```

[`TasksManager/templates/en/public/index.html`](TasksManager/templates/en/public/index.html)
```HTML
<html>
  <head>
    <title>
      Hello World Title
    </title>
  </head>
  <body>
    <h1>
      Hello World Django
    </h1>
    <article>
      Hello world !
    </article>
  </body>
</html>
```

[`TasksManager/views/index.py`](TasksManager/views/index.py)
```python3
from django.shortcuts import render

# Create your views here.
def page(req):
    return render(req, 'en/public/index.html')
```
