#!/bin/bash
url=$1
response_size=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}' | tr -d '\r')
echo "The size of the response body is: $response_size bytes"
