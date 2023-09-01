#!/usr/bin/python3
"""
This module takes a repository name and an owner name,
and uses the GitHub API to display the last recent 10 commits.
"""

if __name__ == '__main__':
    import requests
    from sys import argv
    import json
    repo_name = argv[1]
    owner_name = argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    headers = {'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'}
    res = requests.get(url, headers=headers)
    res_dict = json.loads(res.text)
    for i in range(10):
        print(f"{res_dict.get(i).get('sha')}: \
            {res_dict.get(i).get('commit').get('author').get('name')}")

