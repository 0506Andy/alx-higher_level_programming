#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]  # The URL is taken from the first command-line argument

    response = requests.get(url)  # Send a GET request to the URL
    x_request_id = response.headers.get('X-Request-Id')  # Retrieve the value of X-Request-Id from the headers

    print(x_request_id)  # Print the value of X-Request-Id
