#!/usr/bin/python3

import requests

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():

    # Make HTTP GET request using requests
    # and decode JSON attachment as pythonic data structure
    # Also, append the URL ITEMURL with a parameter to return 1000
    # items in one response
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    healwords = []

    for item in items.get("results"):
        if 'heal' in item.get("name"):
            healwords.append(item.get("name"))

    print(f"There are {len(healwords)} words that contain the word 'heal' in the Pokemon Item API!")
    print("List of Pokemon items containing heal: ")
    print(healwords)

if __name__ == "__main__":
    main()