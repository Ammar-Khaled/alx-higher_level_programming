#!/bin/bash
# This script takes in a URL as an argument, sends a GET request to the URL with a header variable X-School-User-Id with the value 98,
curl -s -H "X-School-User-Id: 98" "$1"
