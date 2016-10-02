import requests
import os

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

def get_restaurants(lat="37.788744", lon="-122.411587", radius="485"):
    """Finds restaurants near given coordinates. 
    
    Radius in meters. Default radius is ~5 min away from default coords.
    """

    access_token = get_access_token()

    base_url = "https://api.yelp.com/v3/businesses/search?"
    search_terms = "latitude=%s&longitude=%s&radius=%s&categories=food"

    # Fetch all restaurant info 
    response = requests.get(base_url + search_terms % (lat, lon, radius),
                            headers={'Authorization': 'Bearer %s' % access_token})

    # Extract just the restaurant names/ids
    restaurants = response.json()['businesses']
    print restaurants
    return restaurants

for restaurant in get_restaurants():
    print restaurant['name']
