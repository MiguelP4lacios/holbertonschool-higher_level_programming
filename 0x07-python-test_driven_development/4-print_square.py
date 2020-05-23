#!/usr/bin/python3
# -*- coding: utf-8 -*-
def print_square(size):

    e_1 = "size must be an integer"
    e_2 = "size must be >= 0"

    if type(size) != int:
        raise TypeError(e_1)
    if size < 0:
        raise ValueError(e_2)
    if type(size) == float and size < 0:
        raise TypeError(e_1)

    for row in range(size):
        print("#" * size)