#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

from pprint import pprint

import requests

URL="https://swapi.dev/api/people/four"

def main():
    """sending GET request, checking response"""

    resp = requests.get(URL)

    vader = resp.json()

    pprint(vader)

if __name__ == '__main__':
    main()