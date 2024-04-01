#!/bin/bash
# This script sends a GET request and displays the body of the response for a 200 status code
if curl -s -f -o response_body "$1"; then
    cat response_body
fi
rm -f response_body
