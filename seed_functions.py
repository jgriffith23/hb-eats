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

        addr_for_search = "+".join([
            str(campus.building),
            street,
            city,
            campus.state,
        ])

        print addr_for_search

        restaurants = yelp_api.get_restaurants(term="lunch")


        # {
        #     u'duration': 
        #     {
        #         u'text': u'2 mins', 
        #         u'value': 128
        #     },
            
        #     u'distance': 
        #     {
        #         u'text': u'0.1 mi', 
        #         u'value': 166
        #     },

        #     u'status': u'OK'
        # }

        # for restaurant in restaurants:
        #     coords = restaurant['coordinates']
        #     if coords.get('latitude') is None:
        #         continue

        #     time_and_distance = gmaps.get_travel_details(end=coords)

        #     name = restaurant['name']
        #     yelp_id = restaurant['id']
        #     miles_away_683 = float(time_and_distance['distance']['text'][:-3])
        #     minutes_away_683 = int(time_and_distance['duration']['text'][:-5])

        # FIXME: Make model for HB campus and model for location_info


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_campuses("seed_data/addresses.csv")
    load_restaurant_distances()
