#!/bin/bash
# This script sends a JSON POST request to a URL passed as the first argument, from a json file passed as second parameter
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
