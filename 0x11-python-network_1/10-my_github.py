#!/usr/bin/python3
"""json api
"""


if __name__ == "__main__":

    import requests
    from sys import argv

    URL = 'https://api.github.com/user'

    auth = (argv[1], argv[2])

    res_json = requests.get(URL, auth=auth).json()
    print(res_json.get('id'))
