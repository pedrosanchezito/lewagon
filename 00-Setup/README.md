# Setup

You will work on Windows 10 with the Le Wagon PCs.

Here is a list of what we already installed for you:

- Google Chrome
- Slack
- **Sublime Text 3** (Unlicensed but unlimited usage) with [Package Control](https://packagecontrol.io/)
- Python 3.7 & [`pipenv`](https://docs.pipenv.org/)
- `git` & **Git Bash**

Your `$PATH` should be all set to work with the required binaries.

Open Git Bash and check some versions:

```bash
git --version
python --version
pipenv --version
```

## Your turn!

There still some configuration left for **you** to do.

### GitHub

We will use your personal public `github.com` account. If you are reading this, it means that you have one and are logged in with it!

We need to create a SSH key on your computer and link it to your GitHub account. At the end of the week, don't forget to remove this key from your GitHub account as this is not your computer. Protecting your key with a strong **passphrase** will guarantee security during the week.

GitHub has handy tutorials. Follow them:

1. [Generate a new SSH key](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-windows)
1. [Add this key to your GitHub account](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/#platform-windows)

To check if this step is done, run:

```bash
ssh git@github.com
```

If it says "Permission denied", call a teacher to help you. If it says "Hi <github_nickname>", you are all set!

## Exercises

Let's start working on the first exercise! Go to [`01-OOP/01-Sum-Of-Three`](../01-OOP/01-Sum-Of-Three). Good luck!

