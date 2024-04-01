#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
It manages urllib.error.HTTPError exceptions and prints "Error code:" followed by the HTTP status code.
"""

import urllib.request
import urllib.error
import sys

# Check if the script is the main program and prevent it from running when imported
if __name__ == "__main__":
    # Take the URL from the command line arguments
    url = sys.argv[1]

    try:
        # Use the with statement to ensure proper acquisition and release of resources
        with urllib.request.urlopen(url) as response:
            # Read the response and decode it
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        # Print the HTTP status code if an HTTPError is encountered
        print(f"Error code: {e.code}")
