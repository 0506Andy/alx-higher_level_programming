#!/bin/bash
url=$1
curl -sIX OPTIONS "$url" | grep "Allow:" | cut -d " " -f2-
