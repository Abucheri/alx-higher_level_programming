#!/usr/bin/python3
"""
Module: 7-error_code
Sends a request to a URL and displays the body of the response
Prints an error message if the HTTP status code is greater than
or equal to 400
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        response = requests.get(url)
        content = response.text
        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(content)
