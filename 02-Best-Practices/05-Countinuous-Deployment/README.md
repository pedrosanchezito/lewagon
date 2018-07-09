# Continuous Deployment

The DevOps graal that teams want to achieve is **Continuous Deployment**. The idea is to configure your hosting environment in such a way that every change in `master` which yields a green build on the Build Automation tool _can_ and _will_ be pushed to production as soon as possible.

In this exercise, we will set up a [**PaaS**](https://en.wikipedia.org/wiki/Platform_as_a_service) to host our longest word game.

## HTTP server

Before pushing our code to a hosting provider, we would like to be able to interact with it. The easiest way to do this is to encapsulate the game around a small HTTP server.

We will build a simple page which will display the random grid. Underneath this grid, a form with an input to type a word, and a submit button.

When clicking the button, the form will be submitted and will reload the page to showcase the results.

![](../../img/longest-word-mockup.png)

Go back to your code, and create a branch to start working on this feature.

```bash
cd ~/code/$YOUR_GITHUB_USERNAME/longest-word

git status # is that clean?
git checkout master
git pull origin master
git branch -d dictionary-api
git checkout -b http-server
```

We are going to use [Flask](http://flask.pocoo.org/), a microframework to quickly build web apps.

```bash
pipenv install flask
touch wsgi.py
subl .
```

Open the `wsgi.py` file and copy paste the following code:

```python
# wsgi.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello world!"
```

You can start this very basic Flask app with:

```bash
FLASK_ENV=development pipenv run flask run
```

Open your browser and go to [localhost:5000](http://localhost:5000/). Is it working, do you get "Hello World" as a text response from the server? If not, call a teacher.

This exercise goal is not about implementing the little application, we will cover Flask in details in tomorrow's lecture. So let's build together our application:

```bash
mkdir static
touch static/style.css
mkdir templates
touch templates/home.html
```

We just created a CSS stylesheet and the HTML template for the Home page. Let's add the business logic in `wsgi.py`:

```python
# wsgi.py
from flask import Flask, render_template
from game import Game

app = Flask(__name__)

@app.route('/')
def home():
    game = Game()
    return render_template('home.html', grid=game.grid)
```

In the code above, we are initializing a new `Game` instance to generate a grid. We pass this grid as a local variable to the `home.html` template, so that we can use it in the view.

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf8" />
    <title>Longest Word</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  </head>
  <body>
    <h1>Longest Word</h1>
    <div>
      {% for letter in grid %}
        <span class="letter">{{ letter }}</span>
      {% endfor %}
    </div>
    <form action="/check" id="form" method="post">
      <input type="hidden" name="grid" value="{{ ''.join(grid) }}">
      <input type="text" name="word">
      <button>Check!</button>
    </form>
  </body>
</html>
```

We give you also some CSS:

```css
/* static/style.css */
body {
  font-family: sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}
.letter {
  border: 1px solid #999;
  padding: 8px 6px;
  width: 24px;
  display: inline-block;
  text-align: center;
  background-color: #333;
  color: #eee;
}
#form, #results {
  margin: 1em 0;
}
.valid {
  color: green;
}
.invalid {
  color: red;
}
```

Phew! Now let's try this, head over to your browser and reload the page. Can you see the grid with a form? Awesome!

If you try to play, you will get an error. It's because we have not implemented the `/check` endpoint yet (the one where the form gets submitted to).

```python
# wsgi.py

# [...]

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word)
```

The idea is that we get the grid (as a hidden field) and the word (the one you typed in the input) from the previous request, then we build a `Game` instance and check if the word is valid. We feed this information back to the `check.html` view to be used to display the results.

💡 We need to actually pass the grid in the `POST` request as HTTP is **stateless**.

```html
<!-- templates/check.html -->
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf8" />
    <title>Longest Word</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  </head>
  <body>
    <h1>Longest Word</h1>
    <h2>Result</h2>
    <div>
      {% for letter in grid %}
        <span class="letter">{{ letter }}</span>
      {% endfor %}
    </div>
    <div id="results">
      Your word: <strong>{{ word }}</strong>.
      {% if is_valid %}
        <span class="valid">Congrats, it's valid!</span>
      {% else %}
        <span class="invalid">Sorry, it's invalid...</span>
      {% endif %}
    </div>
    <div>
      <a href="/">New game</a>
    </div>
  </body>
</html>
```

That's it! Your app should be working correctly. Time to commit, push and _open a Pull Request_ on GitHub:

```bash
git add .
git commit -m "Small web app wrapper around the Game"
git push origin http-server
# head to github.com to open a Pull Request!
```

## Heroku




## Going further

Big PR? New feature?

- [Feature Toggle](https://en.wikipedia.org/wiki/Feature_toggle)
