#!/bin/bash
# This script takes in a URL as an argument,
# sends a GET request to the URL with a header variable X-School-User-Id with the value 98,
# and displays the body of the response

curl -s -H "X-School-User-Id: 98" "$1"

# -s => Silent mode
# -H, --header "name: value" => Pass custom header(s) to server
