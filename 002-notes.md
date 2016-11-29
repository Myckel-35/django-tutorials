[Back](README.md)

# Notes for Chapter 2

Installation: `pip install django==="1.6"` _or just the newest_


## Create Project

```bash
# How to create a new Project
django-admin startproject djale # i created this directory like this
```

> FILES
>
> [djale/settings.py](djale/settings.py)
> Parameters of our Project (debug, db, packages, ...)
> 
> [djale/urls.py](djale/urls.py)
> Include all Project-URLs (routing)


## Create an App in the project

```bash
python manage.py startapp TasksManager
```
> FILES
>
> [TasksManager/__init__.py](TasksManager/__init__.py)
> Defines Package
>
> [TasksManager/admin.py](TasksManager/admin.py)
> Include Models to incorporate with the
> administration module
>
> [TasksManager/models.py](TasksManager/models.py)
> Include Models (Connection to Database) -> Chapter 5
>
> [TasksManager/tests.py](TasksManager/tests.py)
> UnitTests
>
> [TasksManager/views.py](TasksManager/views.py)
> Actions before sending the HTML-Page to Client
