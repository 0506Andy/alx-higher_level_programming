#!/bin/bash
# Sends a POST request with variables and displays the response body
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
