#!/bin/bash
# This script takes a URL, sends a GET request, and displays the body of the response for a 200 status code.
curl -sL -w "%{http_code}" "$1" -o /dev/null | [ "$(cat)" == "200" ] && curl -sL "$1"
