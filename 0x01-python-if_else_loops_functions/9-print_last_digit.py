#!/usr/bin/python3
def print_last_digit(number):

    if number > 0:
        last_num = number % 10
    else:
        last_num = number % -10
        last_num = abs(last_num)
    print("{}".format(last_num), end="")
    return last_num
