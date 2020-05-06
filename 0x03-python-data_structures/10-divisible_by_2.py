#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resul = []
    for e in my_list:
        if e % 2 == 0:
            resul.append(True)
        else:
            resul.append(False)
    return resul
