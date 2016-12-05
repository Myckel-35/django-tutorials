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

## Now we need some Variables

[`TasksManager/views/index.py`](TasksManager/views/index.py)
```python3
from django.shortcuts import render

# Create your views here.
def page(req):
    vars = {
      'hw': "Hallo Welt :)",
      'my_age': 31,
      'capitals': ["Berlin", "London", "Paris", "Washington"]
      }
    return render(req, 'en/public/index.html', vars)
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
      {{ hw }}
    </h1>
    <article>
      My age is {{ my_age }}.
      {% if my_age < 10 %}
        You are a child.
      {% elif my_age < 18 %>
        You are a teenager.
      {% else %}
        You are an adult.
      {% endif %}
    </article>
    <h2>Some capitals</h2>
    <ul>
      {% for city in capitals %}
        <li>{{ city }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

## Next: Templatefilters

[`TasksManager/templates/en/public/index.html`](TasksManager/templates/en/public/index.html)
```HTML
{# ... #}
<p>{{ "HaLLo welt" }}</p>{# Normal #}
<p>{{ "HaLLo welt" | lower }}</p>{# Everything small #}
<p>{{ "HaLLo welt" | upper }}</p>{# Everything big #}
<p>{{ "HaLLo welt" | capfirst }}</p>{# Only the first letter big #}
{# ... #}
```

Just read pluralize filter. Doesn't tested.

## XSS and Autoescape

Autoescape is by default enabled! (some older versions not)

```Python
vars = {
  'js_on': "<script>console.log('autoescape on');</script>",
  'js_off': "<script>console.log('autoescape off');</script>",
  #...
  }
```

```HTML
{# Manual autoescape example #}
{% autoescape on %}
<p>{{ js_on }}</p>
{# {{ js_on|safe }} would execute the code #}
{% endautoescape %}
{% autoescape off %}
<p>{{ js_off }}</p>
{# {{ js_off|escape }} would escape the code #}
{% endautoescape %}
```

This works only on Variables. If you use a String like `{{ "hello" }}` this wouldn't work.

## Linebreaksfilter

```Python
text = <<<ENDL
Hi,

this is just a text with linebreaks
ENDL
# render
```

```HTML
{{ text|linebreaks }}
```

## Truncated String

```HTML
<p>{{ "This is a far too long text"|truncatechars:20 }}</p>
```
Result: `This is a far too...`

## Creating DRY URLs
