#!/usr/bin/python3
"""
This script fetches the status from a given URL using the requests package.
"""

import requests

# Fetch the URL
response = requests.get('https://alx-intranet.hbtn.io/status')

# Display the body of the response
print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.content}")
print(f"\t- utf8 content: {response.text}")
