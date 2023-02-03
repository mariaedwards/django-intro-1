# django

based on [this tutorial](https://www.youtube.com/watch?v=EuBQU_miReM&list=PL_c9BZzLwBRLCpTc20e2pFT1lmbnevegR&index=2)

## Virtual environment

```shell
python -m venv .venv
. .venv/bin/activate
```

## Django

```shell
pip install django
```

### Initiate the project

```shell
django-admin startproject movies .
```

where the package is called `movies`

In settings.py add the name of the package

```py
# Application definition

INSTALLED_APPS = [
    'movies', # <--- this line is added
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

### To activate server

```shell
python manage.py runserver
```

### To get access to /admin

```shell
python manage.py migrate
python manage.py createsuperuser
```

### Add a model

Create models.py and add a model

### Migrations

When a model in model.py changes, run

```shell
python manage.py makemigrations movies
```

To see SQL of the migration applied, run

```shell
python manage.py sqlmigrate movies 0001
```

where `0001` is the id of the migration in the migrations folder

E.g. the output will be

```txt
--
-- Create model Movie
--
CREATE TABLE "movies_movie" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "director" varchar(255) NOT NULL, "genre" varchar(255) NOT NULL, "release_year" smallint unsigned NOT NULL CHECK ("release_year" >= 0), "title" varchar(255) NOT NULL);
COMMIT;
```

After apply the migration

```shell
python manage.py migrate
```

```txt
  Apply all migrations: admin, auth, contenttypes, movies, sessions
Running migrations:
  Applying movies.0001_initial... OK
```

### Adding a table to the admin interface

Add file admin.py, import a model from models.py

```py
from django.contrib import admin
from .models import Movie

admin.site.register(Movie)
```

After restart the server and see the new table in [the admin interface](http://127.0.0.1:8000/admin/)
