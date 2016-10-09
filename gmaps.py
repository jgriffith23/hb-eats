import googlemaps
import os
import requests

def get_travel_details(end, start=("37.788744","-122.411587")):
    """Given a start/end latitudes and logitudes, returns the distance and
    travel time between them.

    Default start coordinates = Hackbright
    """

    dm_api_key = os.environ['GOOGLE_MAPS_DISTANCE_MATRIX_API_KEY']

    # Create strings for URL to access API endpoint
    endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = "?units=imperial&origins=%s,%s&destinations=%s,%s&mode=walking&key=%s" % \
             (start[0], start[1], end['latitude'], end['longitude'], dm_api_key)

    full_response = requests.get(endpoint + params).json()

    # Distill response down to duration/distance
    travel_details = full_response['rows'][0]['elements'][0]

    return {'duration': travel_details['duration']['text'],
            'distance': travel_details['distance']['text']}
