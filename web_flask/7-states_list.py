#!/usr/bin/python3
"""Return string when navigating to root dir"""
from models.state import State
from models import storage
from flask import Flask
from flask import render_template




app = Flask(__name__, template_folder='templates')


@app.route('/states_list', strict_slashes=False)
def list_states():
    return render_template("7-states_list.html", db=storage.all(State))


@app.teardown_appcontext
def tear_down(error):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)