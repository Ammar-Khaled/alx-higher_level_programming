#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument
# and displays the body of the response

curl -s -X DELETE "$1"

# -s => Silent mode
# -X, --request <command> Specify request command (method) to use
