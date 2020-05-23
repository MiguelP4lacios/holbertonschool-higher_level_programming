#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""module say_my_name
"""


def say_my_name(first_name, last_name=""):
    """say_my_name

    Arguments:
        first_name {[type]} -- [description]

    Keyword Arguments:
        last_name {str} -- [description] (default: {""})

    Raises:
        TypeError: [description]
        TypeError: [description]
    """
    e_1 = "first_name must be a string"
    e_2 = "last_name must be a string"

    if type(first_name) != str:
        raise TypeError(e_1)
    if type(last_name) != str:
        raise TypeError(e_2)

    print("My name is {} {}".format(first_name, last_name))
