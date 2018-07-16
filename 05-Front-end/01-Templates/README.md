# Flask templates

In this exercise, we will re-use the yesterday's application from the [01-SQLAlchemy-Recap](../../04-Database/01-SQLAlchemy-Recap) exercise:

```bash
cd ~/code/<github_username>/flask-with-sqlalchemy
```

Make sure your `git status` is clean (`add` and `commit` the WIP), and that your server can still be started:

```bash
FLASK_ENV=development pipenv run flask run
```

## Homepage

The goal of this exercise will be to replace the following action:

```python
@app.route('/')
def hello():
    return "Hello World!"
```

Instead of returning a plain text sentence, we want to actually build a nice html pages. This time, we won't guide you too much to achieve the result, but give you some pointers:

1. We want you to build two pages: a home page with a grid of products (`/`), and a dynamic "show" page with a given product (`/product/:id`)
1. When a user browses the home page, it should be able to easily go to a "show" page with a click on a link
1. Take some time to read the [Flask Templates](http://flask.pocoo.org/docs/1.0/tutorial/templates/) documentation. This is part of the `flask` package
1. Take some time to read more about [Jinja](http://jinja.pocoo.org/docs/2.10/templates/), the templating language used by Flask.
1. You may try to use [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
1. You may want to _enrich_ your `Product` model with a `image_url`. This will allow you to use the [`Card component`](https://getbootstrap.com/docs/4.1/components/card/)
1. Seed **meaningful** information in your database to design your web page with real data (not `lorem ipsum`!)

**NB**: Those endpoints are different from the API endpoints we implemented yesterday. Don't try to tie them together!
