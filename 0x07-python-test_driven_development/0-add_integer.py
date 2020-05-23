#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""[This module contains a function that adds two integers]

    Arguments: a {[type]} -- first value
    Keyword Arguments: b {int} -- second value (default: {98})
"""


def add_integer(a, b=98):
    """This function add a + b
        Returns: int -- add (a + b)
    """
    e_a = "a must be an integer"
    e_b = "b must be an integer"

    if type(a) != int and type(a) != float:
        raise TypeError(e_a)
    if type(b) != int and type(b) != float:
        raise TypeError(e_b)
    return int(a) + int(b)
