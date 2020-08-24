#!/usr/bin/python3
"""hbtn header
"""


if __name__ == "__main__":

    from sys import argv
    import requests

    URL = argv[1]

    res_html = requests.get(URL)

    print(res_html.headers.get('x-request-id'))
