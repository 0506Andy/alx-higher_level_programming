#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys

# Check if the script is the main program and prevent it from running when imported
if __name__ == "__main__":
    # Take the URL and email from the command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email
    values = {'email': email}

    # Encode the values
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')  # Data should be bytes

    # Send a POST request to the URL with the email as a parameter
    req = urllib.request.Request(url, data)

    # Use the with statement to ensure proper acquisition and release of resources
    with urllib.request.urlopen(req) as response:
        # Read the response and decode it
        the_page = response.read().decode('utf-8')
        print(the_page)
