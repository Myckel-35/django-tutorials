[Index](README.md)
[Back](005-notes.md)
[Next](#)

# Chapter 6. Getting a Model's Data with Querysets

No SQL queries, instead over the ORM.
CRUD (Create, Read, Update, Delete) operations.

Just a simple Example how to create a new
Project (Model) in a View

```Python
from TasksManager.models import Project
from django.shortcuts import render

def page(request):
    new_project = Project(title="Tasks Manager with Django",
                          description="Django projectto getting start with Django easily.",
                          client_name="Me")
    new_project.save()
    return render(request, 'en/public/index.html', {'action':'save datas of model'})
```

> ## Quicknote
>
> You could also use the shell to create project instead of
> create it without a form in the view. :)
>
> `python manage.py shell`
>
```
> >>> from TasksManager.models import Project
> >>> new_project = ...
```
>
> [read more of the shell ...](005-notes.md)

## Let's list our projects

[`TasksManager/views/index.py`](TasksManager/views/index.py)
```Python
from TasksManager.models import Project
from django.shortcuts import render

def page(req):
    all_projects = Project.objects.all()
    vars = {'action': "Display all projects",
            'all_projects': all_projects}
    return render(req, 'en/public/index.html', vars)
```

[`TasksManager/templates/en/public/index.html`](TasksManager/templates/en/public/index.html)
```Python
{% extends "en/public/base.html" %}

{% block title %}
Project list
{% endblock %}

{% block content %}
<h3>{{ action }}</h3>

<table>
  <thead>
    <tr>
      <td>ID</td>
      <td>Title</td>
    </tr>
  </thead>
  <tbody>
    {% for project in all_projects %}
    <tr>
      <td>{{ project.id }}</td>
      <td>{{ project.title }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
{% endblock %}
```
You could also filter the projects:

```Python3
pob = Project.objects

pob.filter(client_name="Me")           # exact
pob.filter(client_name__exact="Me")    # exact word (default)
pob.filter(client_name__iexact="me")   # exact case-insensitive
pob.filter(client_name__contains="M")  # contains
pob.filter(client_name__icontains="m") # contains case-insensitive
```
[more ...](https://docs.djangoproject.com/en/1.10/topics/db/queries/#retrieving-specific-objects-with-filters)

### Bored of giving render a hash? Use locals()

Instead of give render a hash with all vars
you could use `locals()`.

```Python3
# ...
def page(req):
  var_a = "hello"
  var_b = "world"
  
  # return render(req, '.../index.html', {'var_a': var_a, 'var_b': var_b}
  return render(req, '.../index.html', locals())
```

> Tip
> Best practices recommend the hash-version. You would only
> use the necessar variables

### .get()

`Project.objects.get(id=1)` is just like the filter but returns
just one object. Raises an error if you don't have exact 1
object.

Instead you could use `Models.objects.filter(...).first()`

## Let's give our project a View

next: Using the get parameter
