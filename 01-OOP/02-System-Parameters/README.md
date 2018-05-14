# System Parameters

Python scripts can read arguments passed on the command line.

## Getting started

```bash
cd ~/code/<your_username>/reboot-python
cd 01-OOP/02-Parameter-Passing
stt # Open the folder in Sublime Text
```

## Some words about `sys.argv`

Consider the following code:

```python
# args.py
import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
```

You can save it to a file `args.py` and run it:

```bash
pipenv run python args.py arg1 arg2 arg3
# Number of arguments: 4 arguments.
# Argument List: ['test.py', 'arg1', 'arg2', 'arg3']
```

[`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv) is a python **list** containing the command line arguments passed to a Python script. `argv[0]` is always the script name.

## Exercise

