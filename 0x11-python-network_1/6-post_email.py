#!/usr/bin/python3
"""
Module: 6-post_email
Sends a POST request to a URL with an email parameter and displays
the response body
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        eload = {'email': email}
        response = requests.post(url, data=eload)
        # print("Your email is:", email)
        print(response.text)
