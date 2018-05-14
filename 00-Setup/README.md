# Setup

## Text Editor

This is where you will write Python, HTML & CSS code. [Grab it](https://www.sublimetext.com/) and install it. It's not free but you can use it `UNREGISTERED` for how long you want. Just hit `Esc` every time the pop-up comes in (~ every 10 file save).

## Python & `pipenv`

The recommended way of install Python nowadays is with [`pipenv`](https://docs.pipenv.org/). It automatically creates and manages a [virtualenv](https://virtualenv.pypa.io/en/stable/) for every project, as well as adds/removes packages from your Pipfile as you install/uninstall packages. It also generates the ever–important Pipfile.lock, which is used to produce deterministic builds.

To create a new project, use this sequence:

```bash
cd ~/code/<your_username>
mkdir new_project && cd $_
pipenv --three # This will create a Pipfile and a virtualenv
```

Then you can easily install dependencies:

```bash
pipenv install nose rednose --dev
pipenv install flask
```

To run a Python program in the context of the releveant virtualenv, run:

```bash
pipenv shell
python file.py
exit # To quit the current virtual env.
```

Or you can do directly:

```bash
pipenv run python file.py
```

Time to add these aliases in your `~/.zshrc`:

```bash
alias pr="pipenv run"
alias prp="pipenv run python"
```
