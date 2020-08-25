#!/usr/bin/python3
"""json api
"""

if __name__ == "__main__":

    import requests
    from sys import argv

    url = 'http://0.0.0.0:5000/search_user'

    q = ""
    if len(argv) == 2:
        q = argv[1]

    data = {'q': q}

    try:
        res = requests.post(url, data).json()

        if res:
            print('[{}] {}'.format(res.get('id'), res.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
