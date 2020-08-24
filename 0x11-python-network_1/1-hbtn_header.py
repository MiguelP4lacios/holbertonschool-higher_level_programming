#!/usr/bin/python3
"""hbtn header
"""


from urllib import request
from sys import argv


with request.urlopen(argv[1]) as response:
    print(response.headers['X-Request-Id'])
