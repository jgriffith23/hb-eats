"""Code that adds new data to a database.

To avoid maxing calls to the Google Maps Distance API and make plotting these
locations on a map easier, store the location data and the distance data.
"""

import yelp_api, gmaps
from model import db, connect_to_db, Restaurant, Campus, Distance
from server import app


def load_campuses(location_info):
    """Add Hackbright campuses to the database."""

    print "Loading campuses."

    Campus.query.delete()

    with open(location_info) as addresses:
        for addr in addresses:
            addr = addr.strip()
            building, street, city, state, zipcode, lat, lon = addr.split(",")

            campus = Campus(building=building,
                            street=street,
                            city=city,
                            state=state,
                            zipcode=zipcode,
                            lat=lat,
                            lon=lon,)
            db.session.add(campus)

        db.session.commit()


def load_restaurant_distances():
    """Add restaurants that are open at 1:00 PM, near a particular address."""

    print "Loading restaurants and distances."

    yelp_api.SEEDING = True

    Restaurant.query.delete()
    Distance.query.delete()

    campuses = Campus.query.all()

    for campus in campuses:

        lat = str(campus.lat)
        lon = str(campus.lon)
        street = "+".join(campus.street.split(" "))
        city = "+".join(campus.city.split(" "))

        search_addr = "+".join([
            str(campus.building),
            street,
            city,
            campus.state,
        ])

        restaurants = yelp_api.get_restaurants(term="lunch", lat=lat, lon=lon)

        for restaurant in restaurants:
            coords = restaurant['coordinates']
            if coords.get('latitude') is None:
                continue

            dist_info = gmaps.get_travel_details(start=search_addr, end=coords)

            name = restaurant['name']
            yelp_id = restaurant['id']

            units_away, units = dist_info['distance']['text'].split(' ')

            if units[-1] == 's':
                units = units[:-1]

            minutes = dist_info['duration']['text'].split(' ')[0]

            rest_record = Restaurant.query.filter_by(name=name).first()
            if not rest_record:
                rest_record = Restaurant(name=name, yelp_id=yelp_id)

            dist_record = Distance(restaurant=rest_record,
                                   campus=campus,
                                   units_away=units_away,
                                   minutes=minutes,
                                   units=units)

            db.session.add_all([rest_record, dist_record])

        db.session.commit()


def reseed_all():
    """Refresh the entire database with accurate data."""

    connect_to_db(app)
    db.drop_all()
    db.create_all()

    load_campuses("seed_data/addresses.csv")
    load_restaurant_distances()


if __name__ == "__main__":
    reseed_all()
