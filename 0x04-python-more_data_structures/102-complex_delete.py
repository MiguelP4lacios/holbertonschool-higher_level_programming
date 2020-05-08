#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    values = list(a_dictionary.values())
    for i, key in enumerate(keys):
        if value is values[i]:
            del a_dictionary[key]
    return a_dictionary
