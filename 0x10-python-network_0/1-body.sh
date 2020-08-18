#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response


status=$(curl -sI "$1" | head -n +1 | awk '{print $2}')

if [ "$status" == "200" ]; then
        curl -L "$1"
fi
