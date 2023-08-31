#!/bin/bash
# This script takes in a URL and displays the size of the body of its response.

curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2

# -s => silent mode
# -I, --head => Show document info (headers) only
