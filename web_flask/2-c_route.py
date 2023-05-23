#!/usr/bin/python3
"""
This script starts a Flask web application.
"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display 'HBNB' message.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display 'C' followed by the value of the text variable.
    Replace underscore _ symbols with a space.
    """
    return 'C ' + escape(text.replace('_', ' '))


if __name__ == '__main__':
    """
    Main entry point of the application.
    """
    app.run(host='0.0.0.0', port=5000)

