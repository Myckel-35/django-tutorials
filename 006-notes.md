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
> create it without a form :)
>
> `python manage.py shell`
>
> ```
> >>> from TasksManager.models import Project
> >>> new_project = ...
```
>
> [read more of the shell ...](005-notes.md)


