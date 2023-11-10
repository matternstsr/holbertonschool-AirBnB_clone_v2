#!/usr/bin/python3
"""Return Hello HBNB when started"""
from flask import Flask
app = Flask(__name__)
@app.route('/', strict_slashes=False)
def say_hello():
    return 'Hello HBNB!'