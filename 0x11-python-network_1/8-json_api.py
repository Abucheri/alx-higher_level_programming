#!/usr/bin/python3
"""
Module: 8-json_api
Sends a POST request to http://0.0.0.0:5000/search_user with
a letter as a parameter
Displays the id and name from the JSON response if it is properly
formatted and not empty
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    lload = {'q': letter}
    response = requests.post("http://0.0.0.0:5000/search_user", data=lload)
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
