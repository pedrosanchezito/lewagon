# SQLAlchemy Recap

Before going back to yesterday's `twitter-api` repository, let's create a brand new Flask app (without the factory pattern `create_app`) and:

1. Add [psycopg2](http://initd.org/psycopg/) to use PostgreSQL
1. Use [SQLAlchemy](https://www.sqlalchemy.org/) as the ORM on top of PostgreSQL
1. Add [Alembic](http://alembic.zzzcomputing.com/) to manage schema migration with the [`Flask-Migrate`](http://flask-migrate.readthedocs.io/) package.
1. Deploy to Heroku

## Postgresql

Head over to [postgresql.org/download/windows/](https://www.postgresql.org/download/windows/) and download the installer for PostgreSQL 10+. Run it. It will install:

- the PostgreSQL Server
- pgAdmin 4, a very useful GUI client to run queries and administrate the server
- Command line tools, useful to install the `psycopg2` package

The setup wizard will ask you for a superadmin password. To simplify the pedagogical experience, knowing that this is a bad security practise, put `admin` as the password.

You should leave the port as the default suggested value (`5432`), and choose `English, United States` as the default locale.

## Python 3.6

The `psycopg2` does not support yet Python 3.7, so we'll install 3.6. [Download the 3.6.6 installer](https://www.python.org/ftp/python/3.6.6/python-3.6.6-webinstall.exe) and run it. When you are done, close all your Git Bash windows.

## Getting started

Let's start a new repository from scratch:

```bash
cd ~/code/<your_username>
mkdir flask-with-sqlalchemy & cd $_
git init
pipenv --python 3.6
pipenv install flask psycopg2 gunicorn Flask-SQLAlchemy Flask-Migrate
```

```bash
touch wsgi.py
subl # Open Sublime Text in the current folder.
```

### Flask Boilerplate

In your `wsgi.py` file, copy paste the following boilerplate:

```python
# wsgi.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"
```

Check that your application is starting with:

```bash
FLASK_ENV=development pipenv run flask run
```

We will need to manipulate many environment variables. Let's use [`https://github.com/theskumar/python-dotenv`]:

```bash
pipenv install python-dotenv --dev
touch .env
echo ".env" >> .gitignore # You don't want to commit your env variables!
```

Let's try this right away. Open the `.env` file in Sublime Text and add a dummy environment variable:

```bash
# .env
DUMMY="dummy"
```

Open the `wsgi.py` file and insert at the beginning of the file the following code:

```bash
# wsgi.py
from dotenv import load_dotenv
import os

load_dotenv()

import logging
logging.warn(os.environ["DUMMY"])

# [...]
```

Relaunch the `flask run` server. You should see this:

```bash
Loading .env environment variables...
# [...]
WARNING:root:dummy
```

See? It automatically populates the `os.environ` with the content of the `.env` file!

**Remove the `import logging` and `logging.warn` lines now**

## `Config` class

As we are introducing a database, we also need to introduce the concept of **environment** and config classes. The idea is that we are going to use three different databases: the development one, the test one and the one on Heroku (production).

To handle all these cases, we can introduce a new file:

```bash
touch config.py
```

```python
# config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
```

In development, we will use the `DevelopmentConfig` class:

```bash
# .env
# you can remove DUMMY
APP_SETTINGS="config.DevelopmentConfig"
```

Once we have this file, we can **bind** the Flask application to SQLAlchemy:

```python
# wsgi.py
# [...]
from flask_sqlalchemy import SQLAlchemy

# [...] After the `app` initialization
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

# [...]
```






