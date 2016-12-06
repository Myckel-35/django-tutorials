[Index](README.md)
[Back](004-notes.md)
[Next](#)

# Notes for Chapter 5

Django uses [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping)

[Django-Docs ORM](https://docs.djangoproject.com/en/1.10/topics/db/)

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
    date_created = models.DateField(verbose_name="Date of Birthday", auto_nod_add=True)
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

## Relationships between models


