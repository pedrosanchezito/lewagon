# Twitter API

Now that we have played a bit with Flask, it's time to start the exercises which will keep us busy for the next three days. The goal is to build a clone of the [Twitter API](https://developer.twitter.com/en/docs/api-reference-index) using Flask and different Flask plugins (like [these](https://github.com/humiaozuzu/awesome-flask)).

⚠️ In this exercise, we will implement some API endpoints with the a big restriction: we don't have a relational database yet! This constraint will help you focus on the HTTP layer of the API, not on the information retrieval. To abstract the database, we will use the [data access object (DAO)](https://en.wikipedia.org/wiki/Data_access_object) pattern and tomorrow we will replace it with actual queries to the database.

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
👉 Do we need the `print()` statement in the test method? Why (not)?

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

## First API endpoint - `/api/v1/tweets/:id`

In the following section, we will implement the HTTP API serving a JSON of a single tweet.

### Model

Before rushing to the Flask blueprint we need to create to serve an HTTP response,
we need a model to hold some data. We don't have a database (yet) so we will
create everything manually today.

Let's think about our `Tweet` and use TDD to implement this class. Have a look at
what [a Tweet is](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-show-id#example-response) and you'll see that is quite complex.
Let's simplify by saying a tweet will hold some `text` and `created_at` date.

### TDD

Let's use TDD to implement this `Tweet` class with its two instance variables. We will write
the test first and then walk our way until the test turns green.

```bash
touch tests/test_models.py
```

```python
# tests/test_models.py
from unittest import TestCase
from app.models import Tweet  # We will code our `Tweet` class in `app/models.py`

class TestTweet(TestCase):
    def test_instance_variables(self):
        # Create an instance of the `Tweet` class with one argument
        tweet = Tweet("my first tweet")
        # Check that `text` holds the content of the tweet
        self.assertEqual(tweet.text, "my first tweet")
        # Check that when creating a new `Tweet` instance, its `created_at` date gets set
        self.assertIsNotNone(tweet.created_at)
        # Check that the tweet's id is not yet assigned when creating a Tweet in memory
        self.assertIsNone(tweet.id)
```

👉 Take some time to read the [26.4. `unittest`](https://docs.python.org/3/library/unittest.html) chapter.

OK, the test is written, let's run the test! (it should not be green):

```bash
pipenv run nosetests tests/test_models.py
```

💡 _In the command above ☝️, we give the exact filename to run only this test file_

You should get something which looks like this:

```bash
======================================================================
1) ERROR: Failure: ModuleNotFoundError (No module named 'app.models')
----------------------------------------------------------------------
    # [...]
    tests/test_models.py line 2 in <module>
      from app.models import Tweet
   ModuleNotFoundError: No module named 'app.models'
```

👉 What's next? **Read the error message and try to fix it**

<details><summary>Reveal answer</summary><p>

You must create the `models.py` file so that this module is defined!

```bash
touch app/models.py
```
</p></details>

Run the tests again **until the error message changes**. You should get this one:

```bash
======================================================================
1) ERROR: Failure: ImportError (cannot import name 'Tweet')
----------------------------------------------------------------------
    # [...]
    tests/test_models.py line 2 in <module>
      from app.models import Tweet
   ImportError: cannot import name 'Tweet'
```

👉 What is the **minimum** code change you can do to fix this error?

<details><summary>Reveal answer</summary><p>

The error complains about the fact that `Tweet` is not defined. The minimum code
change we can do is to create an **empty** class:

```python
# app/models.py
class Tweet:
    pass
```
</p></details>

The next error should be:

```bash
======================================================================
1) ERROR: test_instance_variables (test_models.TestTweet)
----------------------------------------------------------------------
   Traceback (most recent call last):
    tests/test_models.py line 6 in test_instance_variables
      tweet = Tweet("my first tweet")
   TypeError: object() takes no parameters
```

👉 What is the **minimum** code change you can do to fix this error?

<details><summary>Reveal answer</summary><p>

Our `Tweet` class is empty and needs an [instance variable](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables) `text`:

```python
# app/models.py
class Tweet:
    def __init__(self, text):
        self.text = text
```

</p></details>


The next two errors should complain about:

```bash
'Tweet' object has no attribute [...]
```

👉 How can we fix this last two errors and make the test pass?

<details><summary>Reveal answer</summary><p>

Our `Tweet` class is missing the `created_at` instance variable, automatically
set to [the current time](https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python).
It's also missing the `id` instance variable, set to `None` on instance creation.

```python
# app/models.py
from datetime import datetime

class Tweet:
    def __init__(self, text):
        self.id = None
        self.text = text
        self.created_at = datetime.now()
```

</p></details>

✨ Congrats! you juse implemented the `Tweet` class using TDD.

### Repository

We need a model to hold all instances of `Tweet` and assigned auto-incremented ids.
This class will be replaced in the next chapter by a proper [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping)
interacting with a relational database. Until then, we need to **fake** it.


**Specification**: The repository class will hold a list of tweets, empty at first,
but will accept new tweets. When receiving a new tweet, it will automatically assign
to it an auto-incremented id (starting at `1`). The list of tweets will be hold in memory.


Let's use TDD to implement this class!

```bash
touch tests/test_repositories.py
```

👉 This time, try to write the test yourself.

<details><summary>Reveal answer (Really try first 🙏)</summary><p>

```python
# tests/test_repositories.py
from unittest import TestCase
from app.models import Tweet
from app.repositories import TweetRepository

class TestTweetRepository(TestCase):
    def test_instance_variables(self):
        repository = TweetRepository()
        self.assertEqual(len(repository.tweets), 0)

    def test_add_tweet(self):
        repository = TweetRepository()
        tweet = Tweet("a new tweet")
        repository.add(tweet)
        self.assertEqual(len(repository.tweets), 1)

    def test_auto_increment_of_ids(self):
        repository = TweetRepository()
        first_tweet = Tweet("a first tweet")
        repository.add(first_tweet)
        self.assertEqual(first_tweet.id, 1)
        second_tweet = Tweet("a second tweet")
        repository.add(second_tweet)
        self.assertEqual(second_tweet.id, 2)
```

</p></details>

Once the test is written, try to implement the `Tweetrepository` class using the
same TDD technique we used to implement the `Tweet` class.

<details><summary>Reveal answer</summary><p>

```python
# app/repositories.py

class TweetRepository:
    def __init__(self):
        self.tweets = []
        self.next_id = 1

    def add(self, tweet):
        self.tweets.append(tweet)
        tweet.id = self.next_id
        self.next_id += 1
```

💡 See how the test file is way longer than the actual implementation?

</p></details>
