from flask import Flask, render_template, session, jsonify, request
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from model import Campus, Distance, connect_to_db, db
import yelp_api
import os

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def index():
    """Render the homepage."""

    # building = int(request.args.get("building", "683"))

    # # Get the HB campus whose restaurants we want to render.
    # campus = Campus.query.filter_by(building=building).first()

    # # Without eager loading, front page would make 50 queries to render. With
    # # eager loading, it makes 26.
    # distances = Distance.query.options(
    #     db.joinedload('restaurant')).order_by(
    #     Distance.minutes).filter_by(
    #     campus_id=campus.campus_id).all()

    return render_template("index2.html") #, distances=distances, active=building)


@app.route("/restaurants.json")
def get_restauraunts():
    """Return a JSON string with nearby restaurant info."""

    building = int(request.args.get("building", "683"))

    campus = Campus.query.filter_by(building=building).first()

    distances = Distance.query.options(
        db.joinedload('restaurant')).order_by(
        Distance.minutes).filter_by(
        campus_id=campus.campus_id).all()

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

    return jsonify(info=restaurant_distance_info)



#####################################################
# Code that only runs if file is explicitly run
#####################################################

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = os.environ.get("DEBUG") or False

    if app.debug:
        # Use the DebugToolbar
        DebugToolbarExtension(app)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    connect_to_db(app)

    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT)
