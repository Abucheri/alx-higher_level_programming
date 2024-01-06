#!/usr/bin/python3
"""
Module: 0-hbtn_status
Fetches https://alx-intranet.hbtn.io/status using urllib
"""

from urllib import request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", utf8_content)
