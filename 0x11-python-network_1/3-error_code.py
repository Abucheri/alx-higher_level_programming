#!/usr/bin/python3
"""
Module: 3-error_code
Sends a request to a URL and displays the body of the response
Handles urllib.error.HTTPError exceptions and prints the HTTP status code
"""

import sys
from urllib import request, error


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        try:
            with request.urlopen(url) as response:
                body = response.read().decode('utf-8')
                print(body)
        except error.HTTPError as e:
            print("Error code:", e.code)
