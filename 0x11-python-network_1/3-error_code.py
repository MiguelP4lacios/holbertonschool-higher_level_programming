#!/usr/bin/python3
"""hbtn header
"""


if __name__ == "__main__":

    from urllib import request, parse, error
    from sys import argv

    URL = argv[1]

    try:
        with request.urlopen(URL) as response:
            the_page = response.read().decode('utf-8')
            print(the_page)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
