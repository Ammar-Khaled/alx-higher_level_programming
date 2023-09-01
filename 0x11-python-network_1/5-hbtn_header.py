#!/usr/bin/python3
"""
This module takes in a URL,
sends a request to the URL and
displays the value of the 'X-Request-Id' variable
found in the header of the response.
"""

if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
