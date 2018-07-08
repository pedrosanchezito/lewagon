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
ssh -T git@github.com
```

If it says "Permission denied", call a teacher to help you. If it says "Hi <github_nickname>", you are all set!

## Environment

Let's save ourselves sometimes by configuring the environment. Open the `bashrc` file with `vim`:

```bash
vim ~/.profile
```

Enter the `INSERTION` vim mode with `i`. Then copy paste (Shift + Insert) the following the configuration:

```bash
# ~/.profile

# https://github.com/huygn/til/issues/26
env=~/.ssh/agent.env

agent_load_env () { test -f "$env" && . "$env" >| /dev/null ; }

agent_start () {
    (umask 077; ssh-agent >| "$env")
    . "$env" >| /dev/null ; }

agent_load_env

# agent_run_state: 0=agent running w/ key; 1=agent w/o key; 2= agent not running
agent_run_state=$(ssh-add -l >| /dev/null 2>&1; echo $?)

if [ ! "$SSH_AUTH_SOCK" ] || [ $agent_run_state = 2 ]; then
    agent_start
    ssh-add
elif [ "$SSH_AUTH_SOCK" ] && [ $agent_run_state = 1 ]; then
    ssh-add
fi

unset env

# Open Sublime Text from Git Bash
alias subl="/c/Program\ Files/Sublime\ Text\ 3/subl.exe"

# Python specifics
alias python="winpty python" # https://stackoverflow.com/a/33696825/197944
alias pr="pipenv run"
alias prp="pipenv run python"
```

Save and quit with `Esc`, `:wq` and `Enter`. Close and start again Git Bash. It should ask for your SSH key passphrase as it stores it in the SSH agent. This way you won't have to re-type it for every `git` command further on.

## Exercises

This repository contains all the exercises for the week. To work on them, clone them on your laptop. Still in Git Bash, run:

```bash
mkdir -p ~/code/lewagon && cd $_
git clone git@github.com:lewagon/reboot-python.git
cd reboot-python
pwd # This is your exercise repository!
```

This repository has a `Pipfile`. You now can easily install dependencies with the following command:

```bash
pipenv install --dev # to install `packages` **and** `dev-packages`
```

It will create the Virtualenv for this folder, using Python 3.7 as [specified](https://github.com/lewagon/reboot-python/blob/master/Pipfile#L15-L16)

Let's start working on the first exercise! Go to [`01-OOP/01-Sum-Of-Three`](../01-OOP/01-Sum-Of-Three). Good luck!

