#!/bin/bash
url=$1
response=$(curl -s -o response_body -w "%{http_code}" "$url")
if [ "$response" -eq 200 ]; then
    cat response_body
else
    echo "The request did not return a status code of 200."
fi
rm response_body
