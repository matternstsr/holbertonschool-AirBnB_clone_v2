#!/usr/bin/python3
"""Display string depending on the root"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def say_hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def say_hnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def cisnotfun(text):
    text = text.replace('_', ' ')
    return "C {}".format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
