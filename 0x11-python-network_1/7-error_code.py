#!/usr/bin/python3
"""hbtn error
"""


if __name__ == "__main__":

    from sys import argv
    import requests

    URL = argv[1]

    res_html = requests.get(URL)

    if res_html.status_code > 400:
        print("Error code: {}".format(res_html.status_code))
    else:
        print(res_html.text)
