#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return None
    else:
        cmp = my_list[0]
        for e in my_list:
            if e > cmp:
                cmp = e
        return cmp
