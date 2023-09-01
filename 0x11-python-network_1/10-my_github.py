#!/usr/bin/python3
"""
This module takes your GitHub credentials (username and password),
and uses the GitHub API to display your id.
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    import json
    username = argv[1]
    password = argv[2]
    url = 'https://api.github.com/user'
    headers = {'Authorization': f'Bearer {password}',
               'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'}
    res = requests.get(url, headers=headers)
    res_dict = json.loads(res.text)
    try:
        print(res_dict['id'])
    except Error:
        print('None')
