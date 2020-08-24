#!/usr/bin/python3
"""hbtn header
"""


if __name__ == "__main__":

    from urllib import request, parse
    from sys import argv

    URL = argv[1]
    email = argv[2]
    val = {'email': email}
    param = parse.urlencode(val)
    param = param.encode('ascii')
    fullURL = request.Request(URL, param)
    with request.urlopen(fullURL) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
