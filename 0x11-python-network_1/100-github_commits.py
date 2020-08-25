#!/usr/bin/python3
"""json api
"""


if __name__ == "__main__":

    import requests
    from sys import argv

    URL = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])

    res_json = requests.get(URL).json()

    for c in res_json[:10]:
        sha = c.get('sha')
        author = c.get('commit').get('author').get('name')

        print("{}: {}".format(sha, author))
