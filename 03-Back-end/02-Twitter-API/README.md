# Twitter API

Now that we have played a bit with Flask, it's time to start the exercises which will keep us busy for the next three days. The goal is to build a clone of the [Twitter API](https://developer.twitter.com/en/docs/api-reference-index) using Flask and different Flask plugins (like [these](https://github.com/humiaozuzu/awesome-flask)).

⚠️ In this exercise, we will implement some API endpoints with the a big restriction: we don't have a relational database yet! This constraint will help you focus on the HTTP layer of the API, not on the information retrieval. To abstract the database, we will use a [data access object (DAO)](https://en.wikipedia.org/wiki/Data_access_object) and tomorrow we will replace it with actual queries to the database.

## Getting started

Let's start a new Flask project:

```bash
cd ~/code/<your_username>
mkdir twitter-api & cd $_
pipenv install flask
touch wsgi.py
```

### Factory Pattern

In the previous example, we initialized the `Flask` application right in the `wsgi.py`. Doing so, `app` was a global variable. The problem with this approach is it makes it harder to test in isolation. The solution to this problem is to use [Application Factories](http://flask.pocoo.org/docs/patterns/appfactories/), a pattern which will turn useful to make our app more modular (i.e. with multiple "small" files rather than some "big" ones).

👉 Take some time to read [this page of the Flask documentation](http://flask.pocoo.org/docs/patterns/appfactories/)

Let's use this approach:

```bash
mkdir app             # This is our main application's package.
touch app/__init__.py # And open this file in Sublime Text
```

```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello World!"

    return app
```

Then open the `./wsgi.py` file and import this new `create_app` to use it right away:

```python
# ./wsgi.py
from app import create_app

application = create_app()
```

Go ahead and launch the app:

```bash
FLASK_ENV=development pipenv run flask run
```

The server should start. Open your browser and visit [`localhost:5000`](http://localhost:5000). You should see "Hello world!" as a text answer!

### Blueprint

The code in `app/__init__.py` is a copy/paste from the previous exercise, we just took the code and put it into a `create_app` method, returning the instance of `Flask` created. We can do better!

👉 Take some time to read about [Modular Flask Applications with Blueprints](http://flask.pocoo.org/docs/blueprints/).

Let's create a new file to hold a Blueprint for the Homepage of our application. This will act as a placeholder for now and will be enhanced on the last day of this Track.

```bash
mkdir app/main
touch app/main/controllers.py
```

```python
# app/main/controllers.py
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello from a Blueprint!"
```

We can now import our simple blueprint into our main application, like this:

```python
# app/__init.py__
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Remove the previous code using `@app` and replace it with:
    from .main.controllers import main
    app.register_blueprint(main)

    return app
```

If you stopped your server, restart it with:

```bash
FLASK_ENV=development pipenv run flask run
```
Open your browser and visit [`localhost:5000`](http://localhost:5000). You should see "Hello from a Blueprint!" as a text answer!

💡 It's important to understand the `from .main.controllers import main` line which happens before the blueprint registering. The `from .main.controllers` means that we look into the `main/controllers.py` file from the **same** package as the local `__init__.py`. It's a shortcut for `from app.main.controllers`. Then the `import main` means that we import the variable or method `main` defined in this `controllers.py` file (here it's a variable: an instance of `Blueprint`).

### Testing

Let's set up our app so that writing test is easy and TDD is possible:

```bash
pipenv install flask-testing nose rednose --dev
```

Let's create our `tests` folders and a first file

```bash
mkdir tests
mkdir tests/main
touch tests/main/__init__.py
touch tests/main/test_home_view.py
```

```python
# tests/main/test_home_view.py
from flask_testing import TestCase
from app import create_app

class TestHomeView(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_home(self):
        response = self.client.get("/")
        text = response.data.decode()
        print(text)
        self.assertIn("Goodbye", text)
```

Open the terminal and run:

```bash
pipenv run nosetests --nocapture
```

The test should be red!

👉 How can you fix the test to make the command turn green?

### Deployment

We want to use Gunicorn and Heroku for production:

```bash
pipenv install gunicorn
echo "web: gunicorn wsgi --access-logfile=-" > Procfile
```

Finally let's set up git:

```bash
git init
git add .
git commit -m "New flask project boilerplate"
```

And create an app to be deployed on Heroku:

```bash
heroku create --region=eu
git push heroku master

heroku open # Check the app is actually running.
```
