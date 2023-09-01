#!/usr/bin/python3
"""This module  takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)."""

if __name__ == '__main__':
    from urllib.request import urlopen
    from urllib.parse import urlencode
    from sys import argv
    url = argv[1]
    data = {'email': argv[2]}
    data = urlencode(data)
    data = data.encode('utf-8')
    with urlopen(url, data) as res:
        print(res.read().decode('utf-8'))
