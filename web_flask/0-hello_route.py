#!/usr/bin/python3
"""
This script  contains starting a Flask 
web application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display 'Hello HBNB!' as the message.
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    """
    application must be listening on 0.0.0.0, 
port 5000.
    """
    app.run(host='0.0.0.0', port=5000)

