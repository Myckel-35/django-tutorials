[Index](README.md)
[Back](004-notes.md)
[Next](#)

# Notes for Chapter 5

Django uses [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping)

[Django-Docs ORM](https://docs.djangoproject.com/en/1.10/topics/db/)

## Add TasksManager to installed Apps

[`djale/settings.py`](djale/settings.py)
```Python3
# Application definition

INSTALLED_APPS = [
    # ...
    'TasksManager',
]
```

## Settings

Default sqlite3.
For the need of another DB look [here](https://docs.djangoproject.com/en/1.10/ref/settings/#databases).

[`djale/settings.py`](djale/settings.py)
```Python3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## Migrations with South [DEPRECATED]

[From Django 1.7 upwards (here 1.10) Django has migrations built in!](http://south.aeracode.org)

## Create simple models

UserProfile

[`TasksManager/models.py`](TasksManager/models.py)
```Python3
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    login = models.CharField(max_length=25, verbose_name="Login")
    passowrd = models.CharField(max_length=100, verbose_name="Password")
    phone = models.CharField(max_length=20, verbose_name="Phone number", null=True, default=None, blank=True)
    born_date = models.DateField(verbose_name="Born date", null=True, default=None, blank=True)
    last_connection = models.DateTimeField(verbose_name="Date of last connection", null=True, default=None, blank=True)
    email = models.EmailField(verbose_name="Email")
    years_seniority = models.IntegerField(verbose_name="Seniority", default=0)
    date_created = models.DateField(verbose_name="Date of Birthday", auto_now_add=True)
```

> `verbose_name=`
> The name for the form
>
> `models.CharField`
> Characterstring with limited length
>
> `models.TextField`
> Characterstring with unlimited length
>
> `models.IntegerField`
> Integer
>
> `models.DateField`
> Date
>
> `models.DateTimeField`
> date + time (h+m+s)
>
> `models.DecimalField`
> Decimal, optional: can be defindes precisely
>
>> Django creates automatically an ID

ProjectModel


[`TasksManager/models.py`](TasksManager/models.py)
```Python3
class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    client_name = models.CharField(max_length=1000, verbose_name="Client name")
```
 > good pracitce would define a relationship for `client_name`

## Migrate to DB

```
$ python manage.py makemigrations
Migrations for 'TasksManager':
  TasksManager/migrations/0001_initial.py:
    - Create model Project
    - Create model UserProfile

# before megrating it is possible to edit the megrationfiles

$ python manage.py migrate
Operations to perform:
  Apply all migrations: TasksManager, admin, auth, contenttypes, sessions
Running migrations:
  Applying TasksManager.0001_initial... OK
```

[The migration: `TasksManager/migrations/0001_initial.py`](TasksManager/migrations/0001_initial.py)

## Excurse - Django Shell (iPython)

```
$ python manage.py shell

>>> from TasksManager.models import Project

# Create a new Project
>>> p = Project()
>>> p.title = "Project X"
>>> p.description = "Top secret project. WARNING"
>>> p.client_name = "--- NOT LISTED ---"
>>> p.save()

# Load all
>>> Project.objects.all()
->  <QuerySet [<Project: Project object>]>
# like an array

# Load first
>>> x = Project.objects.first()
>>> print(x.title)
-> "Project X"
```

## Relationship between Models

Example of `one-to-many`. One Task belongs to a project but a project can have many tasks.
The other type of relationship is the `one-to-one` and `many-to-many`

[`TasksManager/models.py`](TasksManager/models.py)
```Python3
class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.CharField(max_length=1000, verbose_name="Description")
    time_elapsed = models.IntegerField(verbose_name="Elapsed time", null=True, default=None, blank=True)
    importance = models.IntegerField(verbose_name="Importance")
    project = models.ForeignKey(Project, verbose_name="Project", null=True, default=None, blank=True)
    app_user = models.ForeignKey(UserProfile, verbose_name="User")
```

- A task must not related to a project `null=True`
- A task must relate to a UserProfile `null=False`

## Extending models
