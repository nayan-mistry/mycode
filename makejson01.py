#!/usr/bin/python3
"""Reviewing how to parse json | Alta3 Research"""

import json

def main():
    """runtime code"""

    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)

    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)

if __name__ == "__main__":
    main()