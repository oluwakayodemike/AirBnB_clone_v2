#!/usr/bin/python3
"""
This is a script that starts a Flask web application.
"""

from flask import Flask

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

if __name__ == '__main__':
    """
    Web app listens on 0.0.0.0 port 5000.
    """	
    app.run(host='0.0.0.0', port=5000)
