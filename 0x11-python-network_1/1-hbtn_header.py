#!/usr/bin/python3
import urllib.request
import sys

# This script takes a URL as an argument, sends a request, and displays the X-Request-Id header value
if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.getheader('X-Request-Id'))
