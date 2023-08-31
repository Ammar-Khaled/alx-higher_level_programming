#!/bin/bash
# This script sends a JSON POST request
# to a URL passed as the first argument,
# from a json file passed as second parameter
# and displays the body of the response.

curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"

# -s => Silent mode
# -X, --request <command> => Specify request command (method) to uset.
# -H, --header "name: value" => Pass custom header(s) to server
# -d, --data <data> => (HTTP) Sends the specified data in a POST request to the HTTP server.
