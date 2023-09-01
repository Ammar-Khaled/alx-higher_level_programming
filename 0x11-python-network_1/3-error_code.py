#!/usr/bin/python3
"""
This module takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response with HTTPError handling."""

if __name__ == '__main__':
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from sys import argv
    url = argv[1]
    try:
        with urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')
