#!/usr/bin/python3
"""Return string when navigating to root dir"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__, template_folder='templates')


@app.route('/cities_by_states', strict_slashes=False)
def list_state_cities():
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def tear_down(error):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
