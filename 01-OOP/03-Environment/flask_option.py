# pylint: disable=missing-docstring

import os

def start():
    if os.getenv('FLASK_ENV') == 'development':
        return "Starting in development mode..."
    return "Starting in production mode..."

if __name__ == "__main__":
    print(start())
