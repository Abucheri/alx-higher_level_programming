#!/usr/bin/python3
"""
Module: 5-hbtn_header
Sends a request to a URL and displays the value of the X-Request-Id variable
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
