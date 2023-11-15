#!/usr/bin/python3
"""star of a Flask web app"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder='templates')


@app.route('/hbnb_filters', strict_slashes=False)
def states_list():
    """ Creates a sorted list of states and amenities
    for rendering in the template """
    amenities = storage.all("Amenity")
    states = storage.all("State")
    return (render_template('10-hbnb_filters.html', states=states,
                            amenities=amenities))

@app.teardown_appcontext
def teardown(exception):
    """ Closes the storage connection """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
