from flask import Flask, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from model import Campus, connect_to_db
import yelp_api


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Render the homepage."""

    print "\n\n", session, "\n <3 from index\n\n"

    campuses = Campus.query.all()

    hb_683 = campuses[0]

    distances = hb_683.distances

    restaurants = {}

    for distance in distances:
        restaurant = distance.restaurant
        print restaurant.name
        details = yelp_api.get_restaurant(restaurant.yelp_id)
        restaurants[restaurant.name] = {'distance': distance,
                                        'details': details,
                                        'name': restaurant.name}

    return render_template("index.html", restaurants=restaurants)

    # return jsonify(restaurants['Matador']['details'])

#####################################################
# Code that only runs if file is explicitly run
#####################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    TEMPLATES_AUTO_RELOAD = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    connect_to_db(app)

    app.run()
