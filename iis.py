#!/usr/bin/python3

## for making HTTP requests
## python3 -m pip install requests
import requests

## for working with data in lots of formats
## python3 -m pip install pandas
import pandas

from datetime import datetime

import reverse_geocoder as rg

ITEMURL = "http://api.open-notify.org/iss-now.json"

def main():

    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    # Also, append the URL ITEMURL with a parameter to return 1000
    # items in one response
    items = requests.get(f"{ITEMURL}").json()
    
    lat = items["iss_position"]["latitude"]
    lon = items["iss_position"]["longitude"]
    timestamp = items["timestamp"]
    coords_tuple= (lat, lon)

    print(f"""
        CURRENT LOCATION OF THE ISS:
        Lon: {lon}
        Lat: {lat}
        Time: {datetime.fromtimestamp(timestamp)}
        City: {rg.search(coords_tuple, verbose=False)[0]["name"]}
        """)

if __name__ == "__main__":
        main()
