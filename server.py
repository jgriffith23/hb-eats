from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import yelp
import gmaps


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Render the homepage."""

    restaurants = yelp.get_restaurants()
    restaurant_travel_details = {}
    print "\n*********************************************************"
    for restaurant in restaurants:
        print "Getting travel info for %s..." % restaurant['name']
        coords = restaurant['coordinates']
        travel_details = gmaps.get_travel_details(coords)
        restaurant_travel_details[restaurant['name']] = travel_details
    print "*********************************************************\n"

    return render_template("index.html",
                           restaurants=restaurants,
                           restaurant_travel_details=restaurant_travel_details)

#####################################################
# Code that only runs if file is explicitly run
#####################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    TEMPLATES_AUTO_RELOAD = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()
