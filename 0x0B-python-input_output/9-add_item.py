#!/usr/bin/python3
"""Module load, add and save
"""

from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = 'add_item.json'

try:
        my_list = load_from_json_file(filename)
except FileNotFoundError:
        my_list = []
words = argv[1:]
for word in words:
        my_list.append(word)

save_to_json_file(my_list, filename)
