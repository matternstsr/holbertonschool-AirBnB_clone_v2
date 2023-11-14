#!/usr/bin/python3
"""Return string when navigating to root dir"""
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__, template_folder='templates')


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    data = storage.all("State").values()
    states = sorted(data, key=lambda state: state.name)
    return (render_template('9-states.html', states=states))


@app.route('/states/<id>')
def state_cities(id):
    state = storage.get("State", id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return (render_template('9-states.html', state=state, cities=cities))
    else:
        return render_template('9-states.html', nf=True)


@app.teardown_appcontext
def tear_down(error):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
