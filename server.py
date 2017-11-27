from flask import Flask, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from model import Campus, Distance, connect_to_db, db
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

    # Without eager loading, front page would make 50 queries to render. With
    # eager loading, it makes 26.
    distances = Distance.query.options(
        db.joinedload('restaurant')).order_by(
        Distance.minutes).filter_by(
        campus_id=hb_683.campus_id).all()

    return render_template("index.html", distances=distances)

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
