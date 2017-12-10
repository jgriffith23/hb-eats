from flask import Flask, render_template, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from model import Campus, Distance, connect_to_db, db
import os

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Render the homepage."""

    return render_template("index2.html")


@app.route("/restaurants")
def get_restauraunts():
    """Return a JSON string with nearby restaurant info."""

    # The query will tell us which building we're querying for. Default to
    # the first campus, numerically.

    building = int(request.args.get("building", "450"))
    campus = Campus.query.filter_by(building=building).first()

    # Get all restaurant distance info associated with the campus requested.
    distances = Distance.query.options(
        db.joinedload('restaurant')).order_by(
        Distance.minutes).filter_by(
        campus_id=campus.campus_id).all()

    # Create a list of dictionaries representing each restaurant's information
    # so we can JSONify it for the front end.
    restaurant_distance_info = []

    for distance in distances:
        categories = [category.category for category in distance.restaurant.categories]

        all_info = {
            "name": distance.restaurant.name,
            "yelpURL": distance.restaurant.yelp_url,
            "categories": categories,
            "dollarSigns": distance.restaurant.dollar_signs,
            "address": distance.restaurant.address,
            "distanceAway": str(distance.units_away) + " " + distance.units,
            "timeAway": str(distance.minutes) + " min",
            "img": distance.restaurant.img_url,
        }

        restaurant_distance_info.append(all_info)

    return jsonify(restaurants=restaurant_distance_info)


@app.route("/campuses")
def get_campuses():
    """Return JSON containing all campuses."""

    # The query will tell us which campus is going to be displayed.
    active = request.args.get("building")

    campuses = Campus.query.all()

    # Make a list of dictionaries containing campus data that we'll JSONify.
    campuses = [{"building": str(campus.building),
                 "street": campus.street} for campus in campuses]

    # Set the "active" key on each campus dict, so React
    # can render the tabs properly.

    campuses.sort(key=lambda campus: campus["building"])

    # If we landed on the homepage without clicking a tab, default to the
    # first campus in the list.
    if active == "unset":
        active = campuses[0]["building"]

    print active
    print campuses
    print active

    for campus in campuses:
        if campus["building"] == active:
            campus["active"] = True

        else:
            campus["active"] = False

    return jsonify(campuses=campuses)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = os.environ.get("DEBUG") or False

    if app.debug is True:
        # Use the DebugToolbar
        DebugToolbarExtension(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    connect_to_db(app)

    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, threaded=True)
