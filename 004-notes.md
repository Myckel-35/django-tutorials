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

added new url '/connection':

* edited: added url [`djale/urls.py`](djale/urls.py)
* created: [`TasksManager/views/connection.py`](TasksManager/views/connection.py)
* created: [`TasksManager/templates/en/public/connection.html`](TasksManager/templates/en/public/connection.html)

[`djale/urls.py`](djale/urls.py)
```Python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TasksManager.views.index.page, name="public_index"),
    url(r'^index$', TasksManager.views.index.page),
    url(r'^connection$', TasksManager.views.connection.page, name="public_connection"),
]
```

now we give two urls names: `public_index` and `public_connection`


[`TasksManager/templates/en/public/connection.html`](TasksManager/templates/en/public/connection.html)
```Html
<a href="{% url 'public_index' %}">Main</a>,
<a href="{% url 'public_connection' %}">Connection</a>
```

Now we can use these names for our hrefs.

For urls with params this syntax is valid:

```Html
<a href="{% url 'one_param_site' param1 %}">Main</a>,
<a href="{% url 'two_param_site' param1, param2 %}">Connection</a>
```

## Extending the templates

[`TasksManager/templates/en/public/base.html`](TasksManager/templates/en/public/base.html)
```HTML
<html>
  <body>
    {% block title %}<h1>Title in title block</h1>{% endblock %}
    <p>BASE.HTML START</p>
    {% block content %}{% endblock %}
    <p>BASE.HTML ENDE</p>
  </body>
</html>
```

[`TasksManager/templates/en/public/index.html`](TasksManager/templates/en/public/index.html)
```HTML
{% extends "en/public/base.html" %}

{% block title %}
<p>block title: before super</p>
{{ block.super }}
<p>block title: after super</p>
{% endblock %}

{# RESULT of titleblock
<p>block title: before super</p>
<h1>Title in title block</h1>
<p>block title: after super</p>
#}

{% block content %}
{# ... normal content ... #}
{% endblock %}
```

[More on 'extends' ...](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#extends)

[See 'include' for Snippets ...](https://docs.djangoproject.com/en/1.10/ref/templates/builtins/#include)

## Static Files in Templates
