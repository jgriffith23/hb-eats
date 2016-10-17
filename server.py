from flask import Flask, render_template, session
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
import yelp_api
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

    # Fetch a list of restaurants near HB
    restaurants = yelp_api.get_restaurants(term="lunch")

    # To avoid maxing out gmaps API calls, store travel details in the
    # user's session.
    if "travel_details" not in session:
        travel_details = {}

        # Use gmaps distance matrix API to get the time/distance from HB
        # on foot for each restaurant.
        for restaurant in restaurants:

            coords = restaurant['coordinates']
            time_and_distance = gmaps.get_travel_details(end=coords)
            travel_details[restaurant['name']] = time_and_distance
        session["travel_details"] = travel_details

    return render_template("index.html", restaurants=restaurants, travel_details=session["travel_details"])


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
