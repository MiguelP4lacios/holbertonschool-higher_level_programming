#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_num = number % 10
else:
    last_num = number % -10

print("Last digit of {} is ".format(number), end="")

if last_num < 6 and last_num != 0:
    print("{} and is less than 6 and not 0".format(last_num))
if last_num > 5:
    print("{} and is greater than 5".format(last_num))
if last_num == 0:
    print("{} and is 0".format(last_num))
