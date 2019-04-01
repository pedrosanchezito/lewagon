# pylint: disable=missing-docstring

import sys

def main():
    string_to_eval = ""
    for value in sys.argv[1:]:
        string_to_eval += value + " "
    return eval(string_to_eval)

if __name__ == "__main__":
    print(main())
