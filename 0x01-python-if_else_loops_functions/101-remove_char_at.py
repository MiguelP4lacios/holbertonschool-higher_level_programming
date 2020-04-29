#!/usr/bin/python3
def remove_char_at(str, n):
    if n < len(str) and n >= 0:
        new_str = str[:n] + str[1 + n:]
        return new_str
    else:
        return str
