#!/usr/bin/python3
"""
This module takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response with HTTPError handling.
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    url = argv[1]
    r = requests.get(url)
    if (r.status_code >= 400):
        print(f'Error code: {r.status_code}')
    else:
        print(r.text)
