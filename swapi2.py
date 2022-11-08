#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

from pprint import pprint

import requests

#URL="https://swapi.dev/luke/force"
URL= "https://swapi.dev/api/people/4/"

def main():
    """sending GET request, checking response"""

    resp = requests.get(URL)

    if resp.status_code == 200:
        vader = resp.json()
        pprint(vader)
    else:
        print("This is not a valid url.")

if __name__ == '__main__':
    main()