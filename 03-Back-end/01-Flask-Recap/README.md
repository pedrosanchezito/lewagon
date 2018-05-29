# Flask Recap

![](http://flask.pocoo.org/static/logo/flask.png)

[Flask](http://flask.pocoo.org/) is a **microframework** for Python to quickly build a web application.

In this exercise, we will quickly go over every important features of Flask.

## Getting started

You will work in a dedicated repository to apply the best practices covered in the previous lecture.

```bash
cd ~/code/<your_username>
mkdir flask-101 & cd $_
pipenv install flask gunicorn
touch app.py
stt # Open Sublime Text
```

### Flask Boilerplate

In your `app.py` file, copy paste the following boilerplate:

```python
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"
```

What does this code do?

1. First we imported the Flask class. An instance of this class will be our Web application.
1. Next we create an instance of this class. The first argument is the name of the application’s module or package.
1. We then use the `route()` decorator to tell Flask what URL should trigger our function.
1. The function is given a name which is also used to generate URLs for that particular function, and returns the message we want to display in the user’s browser.

### Development run

Go back to your terminal and run:

```bash
FLASK_DEBUG=1 pipenv run flask run
```

The server should start. Open your browser and visit [`localhost:5000`](http://localhost:5000). You should see "Hello world!" as a text answer!

Try to edit the code and reload the page in the browser. 💡 What is happenning?

### Production run

We can test the production configuration with:

```bash
# Ctrl-C to kill the previous server
pipenv run gunicorn app:app --access-logfile=-
```

Open your browser and visit [`localhost:8000`](http://localhost:8000). Again you should see "Hello world!".

Try to edit the code and reload the page in the browser. 💡 What is happenning?

## Heroku

Let's try to deploy this application to Heroku:

```bash
echo "web: gunicorn app:app --access-logfile=-" > Procfile

git init
git add .
git commit -m "First deployment of Flask boilerplate"

heroku create --region=eu
git push heroku master

heroku open                # Do you get an "Hello world?"
heroku logs -n 1000 --tail # Check the access logs are coming up
```
