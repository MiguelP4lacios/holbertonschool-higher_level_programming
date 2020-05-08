#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    if max(a_dictionary, key=lambda k: a_dictionary[k]) is 0:
        return None
    return max(a_dictionary, key=lambda k: a_dictionary[k])
