"""Database models for HB Eats."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Restaurant(db.Model):
    """A restaurant near Hackbright."""

    __tablename__ = "restaurants"

    restaurant_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64))
    yelp_id = db.Column(db.String(64))

    def __repr__(self):
        """A sane representation of a restaurant object."""

        return "<Restaurant {name}>".format(name=self.name)


class Campus(db.Model):
    """A Hackbright campus location."""

    __tablename__ = "campuses"

    campus_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    building = db.Column(db.Integer)
    street = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.String(5))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __repr__(self):
        """A sane representation of a campus object."""

        return "<Campus {building} {street} {city} {state}>".format(
            building=self.building,
            street=self.street,
            city=self.city,
            state=self.state
        )


class Distance(db.Model):
    """How far away from a Hackbright Campus is a Restaurant?"""

    __tablename__ = "distances"

    dist_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    campus_id = db.Column(db.Integer,
                          db.ForeignKey("campuses.campus_id"))
    restaurant_id = db.Column(db.Integer,
                              db.ForeignKey("restaurants.restaurant_id"))
    units_away = db.Column(db.Float)
    units = db.Column(db.String(5))
    minutes = db.Column(db.Float)

    restaurant = db.relationship('Restaurant', backref='distances')
    campus = db.relationship('Campus', backref='distances')

    def __repr__(self):
        """A sane representation of a distance object."""

        return "<Distance ({build} {st}) -- ({restaurant}): ~{num} {units}>".format(
            build=self.campus.building,
            st=self.campus.street,
            restaurant=self.restaurant.name,
            num=self.units_away,
            units=self.units,
        )


def connect_to_db(app, uri="postgresql:///hbeats"):
    """Connect to the database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app

    connect_to_db(app)

    print "Connected to HB Eats database."
