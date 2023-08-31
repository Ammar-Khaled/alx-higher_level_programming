#!/bin/bash
# This script sends a request to a URL passed as an argument,
# and displays only the status code of the response.

curl -s -o /dev/null -w "%{http_code}" "$1"

# -s => Silent mode
# -o, --output <file> => Write to file instead of stdout
# -w/--write-out <format> => get from the file one of these variables:
# url_effective http_code time_total ect.
