#!/usr/bin/python3
"""
This module takes in a letter,
sends a POST request to http://0.0.0.0:5000/search_user,
with the letter as a parameter.
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    import json
    url = "http://0.0.0.0:5000/search_user"
    letter = argv[1] if argv[1] else ""
    res = requests.post(url, {"q": letter})
    if (res.headers['Content-Type'] != 'application/json'):
        print('Not a valid JSON')
    elif (res.text == '{}\n'):
        print('No result')
    else:
        res_dict = json.loads(res.text)
        print(f'[{res_dict["id"]}] {res_dict["name"]}')
