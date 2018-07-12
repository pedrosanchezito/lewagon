# Flask templates

In this exercise, we will re-use the yesterday's application from the [01-SQLAlchemy-Recap](../../04-Database/01-SQLAlchemy-Recap) exercise:

```bash
cd ~/code/<github_username>/flask-with-sqlalchemy
```

Make sure your `git status` is clean (`add` and `commit` the WIP), and that your server can still be started:

```bash
pipenv FLASK_ENV=development pipenv run flask run
```

## Homepage

The goal of this exercise will be to replace the following action:

```python
@app.route('/')
def hello():
    return "Hello World!"
```
