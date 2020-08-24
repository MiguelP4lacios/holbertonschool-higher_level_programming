#!/usr/bin/python3
"""hbtn status
"""


import requests


res_html = requests.get('https://intranet.hbtn.io/status')

print("Body response:")
print("\t- type: {}\n\t- content: {}".format(
        type(res_html.text), res_html.text))
