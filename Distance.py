from math import radians, cos, sin, asin, sqrt
import numpy as np

AVG_EARTH_RADIUS = 6371  # in km


def haversine(point1_lat, point1_long, point2_lat, point2_long, miles=False):
    """ Calculate the great-circle distance bewteen two points on the Earth surface.

    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance bewteen the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.

    """
    h=np.empty(len(point1_lat))
    # unpack latitude/longitude and convert to radians
    for i in range(len(point1_lat)):
        lat1 = radians(point1_lat.iloc[i])
        lng1 = radians(point1_long.iloc[i])
        lat2 = radians(point2_lat.iloc[i])
        lng2 = radians(point2_long.iloc[i])

    # convert all latitudes/longitudes from decimal degrees to radians
        #lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
        lat = lat2 - lat1
        lng = lng2 - lng1
        d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
        h[i] = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
    if miles:
        return h * 0.621371  # in miles
    else:
        return h  # in kilometers

