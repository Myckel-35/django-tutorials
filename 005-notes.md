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

[From Django 1.7 upwards (here 1.10) Django has migrations built in!](south.aeracode.org)

## Create simple models
