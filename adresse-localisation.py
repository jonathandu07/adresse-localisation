#generate gps coordinates using python
from geopy.geocoders import Nominatim

import pandas as pd

#get the coordinates of the address

def get_coordinates(address):
    geolocator = Nominatim(user_agent="myapplication")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude

# print the coordinates of the address
def print_coordinates(address):
    lat, lon = get_coordinates(address)
    print("Latitude: ", lat)
    print("Longitude: ", lon)

get_coordinates("1600 Amphitheatre Parkway, Mountain View, CA")
print_coordinates("1600 Amphitheatre Parkway, Mountain View, CA")