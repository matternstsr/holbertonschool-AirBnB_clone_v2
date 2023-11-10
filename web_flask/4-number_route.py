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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<n>', strict_slashes=False)
def isanumber(n):
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
