#!/usr/bin/python3
"""Return string when navigating to root dir"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__, template_folder='templates')


@app.route('/states_list', strict_slashes=False)
def states_list():
    stored = storage.all("State").values()
    states = sorted(stored, key=lambda state: state.name)
    return (render_template('7-states_list.html', states=states))

@app.teardown_appcontext
def tear_down(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
