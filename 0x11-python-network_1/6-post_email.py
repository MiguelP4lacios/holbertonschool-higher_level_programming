#!/usr/bin/python3
"""hbtn post
"""


if __name__ == "__main__":

    from sys import argv
    import requests

    URL = argv[1]
    email = argv[2]

    data = {'email': email}

    res_html = requests.post(URL, data=data)

    print(res_html.text)
