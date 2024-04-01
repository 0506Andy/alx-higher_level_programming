#!/bin/bash
# This script sends a GET request and displays the body of the response for a 200 status code
curl -s -f "$1" || echo "The request did not return a status code of 200."
