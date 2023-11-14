#!/usr/bin/python3
"""Display string number or template depending on the root"""
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


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


@app.route('/number/<int:n>', strict_slashes=False)
def isanumber(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemplate(n):
    return render_template('5-number.html', value=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd_int_template(n):
    itseven = n % 2 == 0
    return render_template('6-number_odd_or_even.html', value=n, even=itseven)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
