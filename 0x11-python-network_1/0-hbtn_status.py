#!/usr/bin/python3
"""This module fetches a URL."""

if __name__ == '__main__':
    from urllib.request import urlopen
    url = 'https://alx-intranet.hbtn.io/status'
    with urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print(f'\t- type: {type(html)}')
        print(f'\t- content: {html}')
        print(f'\t- utf8 content: {html.decode("utf-8")}')
