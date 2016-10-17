import os
import googlemaps
import googlemaps.distance_matrix as gmaps_dm


def get_travel_details(end="611+Post+St+San+Francisco+CA",
                       start="683+Sutter+St+San+Francisco+CA"):
    """Given start/end addresses, returns the distance and travel time between them
    as a dictionary.

    Default start coordinates = Hackbright

    Returned data is formatted as:
    {u'duration': {u'text': u'2 mins', u'value': 128},
     u'distance': {u'text': u'0.1 mi', u'value': 166},
     u'status': u'OK'}
    """

    # Create a client to pass to Google Maps services calls.
    client = googlemaps.Client(key=os.environ['GOOGLE_MAPS_DISTANCE_MATRIX_API_KEY'])

    # Create a distance matrix to get the travel data.
    matrix = gmaps_dm.distance_matrix(client=client,
                                      units="imperial",
                                      origins=start,
                                      destinations=end,
                                      mode="walking")

    """
    Matrix comes back in the following form:

    {u'status': u'OK',
     u'rows': [{u'elements': [{u'duration': {u'text': u'2 mins', u'value': 128},
                               u'distance': {u'text': u'0.1 mi', u'value': 166},
                               u'status': u'OK'}]}],
                u'origin_addresses': [u'683 Sutter St, San Francisco, CA 94102, USA'],
                u'destination_addresses': [u'611 Post St, San Francisco, CA 94109, USA']}
    """

    # We only want the duration and distance info, so only return those.
    return matrix['rows'][0]['elements'][0]
