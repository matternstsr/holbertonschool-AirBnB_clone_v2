#!/usr/bin/python3
"""Return string when navigating to root dir"""

from flask import render_template
from flask import jsonify

"""In Flask, jsonify is a function that returns a JSON response.
It is commonly used to convert a Python dictionary or other
JSON-serializable object into a JSON-formatted response that
can be sent to the client. This function also sets the appropriate
Content-Type header for the response, indicating that the response
contains JSON data."""

@app.route('/cities_by_states', methods=['GET'], strict_slashes=False)
def cities_by_states():
    """Creates sorted list of states by name"""
    states = get_sorted_states()
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', methods=['GET'])
def state_cities(id):
    """Creates sorted list of cities by name for state"""
    state = get_state_by_id(id)
    if state:
        cities = get_sorted_cities(state.cities)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', nf=True)

def get_sorted_states():
    """get states from storage, sort alpha, return sorted list."""
    data = storage.all("State").values()
    return sorted(data, key=lambda state: state.name)

def get_state_by_id(id):
    """Retrieve a state by its ID from storage."""
    return storage.get("State", id)

def get_sorted_cities(cities):
    """Sort a list of cities alphabetically by name."""
    return sorted(cities, key=lambda city: city.name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
