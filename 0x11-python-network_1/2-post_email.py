#!/usr/bin/python3
"""
Module: 2-post_email
Sends a POST request to a URL with an email parameter and displays
the response body
"""

import sys
from urllib import request, parse


if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        data = parse.urlencode({'email': email}).encode('utf-8')
        reqst = request.Request(url, data=data, method='POST')
        with request.urlopen(reqst) as response:
            body = response.read().decode('utf-8')
            # print("Your email is:", email)
            print(body)
