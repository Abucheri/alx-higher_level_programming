#!/usr/bin/python3
"""
Module: 10-my_github
Uses the GitHub API to display the user id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]
        url = "https://api.github.com/user"
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        try:
            user_data = response.json()
            if 'id' in user_data:
                print(user_data['id'])
            else:
                print("None")
        except ValueError:
            print("None")
