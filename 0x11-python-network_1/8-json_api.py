#!/usr/bin/python3
"""
This script takes in a letter and sends a POST request to a specified URL with the letter as a parameter.
The letter is sent in the variable 'q'. If no argument is given, 'q' is set to an empty string.
If the response body is properly JSON formatted and not empty, it displays the id and name.
Otherwise, it displays 'Not a valid JSON' if the JSON is invalid or 'No result' if the JSON is empty.
"""

import requests
import sys

if __name__ == "__main__":
    # The URL to send the POST request to
    url = 'http://0.0.0.0:5000/search_user'
    
    # The letter to send as a parameter, default to an empty string if no argument is given
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # The payload to send in the POST request
    payload = {'q': letter}
    
    # Send the POST request
    response = requests.post(url, data=payload)
    
    try:
        # Try to load the response as JSON
        json_response = response.json()
        
        # Check if the JSON response is empty
        if json_response:
            # If not empty, print the id and name
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            # If empty, print 'No result'
            print("No result")
    except ValueError:
        # If the response is not valid JSON, print 'Not a valid JSON'
        print("Not a valid JSON")

