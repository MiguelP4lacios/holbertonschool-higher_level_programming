#!/usr/bin/python3
def roman_to_int(roman_string):
    symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    for c1, c2 in zip(roman_string, roman_string[1:]):
        if symbols[c1] < symbols[c2]:
            num -= symbols[c1]
        else:
            num += symbols[c1]
    num += symbols[roman_string[-1]]
    return num
