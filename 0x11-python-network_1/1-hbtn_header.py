#!/usr/bin/python3
"""hbtn header
"""


from urllib import request
from sys import argv


URL = str(argv[1])


with request.urlopen(URL) as response:
    print(response.headers['X-Request-Id'])
