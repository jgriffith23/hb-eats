import requests
import os
from flask import session

SEEDING = False

# Special thanks to aninahpets and her amazing project Fuder, which I looked
# to for code examples. https://github.com/aninahpets/Fuder


def get_access_token():
    """Fetches the OAuth2 access token from Yelp."""

    # Request the access token using app's id and secret
    response = requests.post('https://api.yelp.com/oauth2/token',
                             data={'grand_type': 'client_credentials',
                                   'client_id': os.environ['YELP_APP_ID'],
                                   'client_secret': os.environ['YELP_APP_SECRET']})

    return response.json()['access_token']


def get_restaurants(term, lat="37.788744", lon="-122.411587", radius="805"):
    """Finds restaurants near given lat/lon.

    Radius in meters. Default radius is ~15 min away from default lat/lon.

    Note: Using lat/lon because radius doesn't work properly with an address.
    """

    # Create OAuth2 token and store in session (we don't need to get a new one
    # for every API request)

    access_token = get_access_token()
    
    if not SEEDING:
        if "access_token" not in session:
            session["access_token"] = get_access_token()

    base_url = "https://api.yelp.com/v3/businesses/search"

    # Set parameters for our request to the business search API.
    parameters = {
        "latitude": lat,
        "longitude": lon,
        "radius": radius,
        "term": term,
        "categories": "restaurants",
        "limit": 20,
        "price": "1,2,3",
        "sort_by": "distance",
        # "open_now": "true",
        "open_at": 1500494400,  # 1:30 PM on 7/14/2017, no timezone
    }

    # FIXME: Store resulting JSON data in database...

    # Fetch all restaurants that fit these parameters and capture the response.
    response = requests.get(url=base_url,
                            params=parameters,
                            headers={'Authorization': 'Bearer %s' % access_token})
    print "\n\n\nTHE STUFF\n"
    print response.json()
    print "\n\n\n\n"

    # Extract just the business info.
    return response.json()['businesses']
