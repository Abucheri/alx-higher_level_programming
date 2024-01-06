#!/usr/bin/python3
"""
Module: 1-hbtn_header
Sends a request to a URL and displays the value of the X-Request-Id variable
"""

import sys
from urllib import request


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        with request.urlopen(url) as response:
            x_request_id = response.info().get('X-Request-Id')
            print(x_request_id)
