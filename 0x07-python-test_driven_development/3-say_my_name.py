#!/usr/bin/python3
# -*- coding: utf-8 -*-
def say_my_name(first_name, last_name=""):

    e_1 = "first_name must be a string" 
    e_2 = "last_name must be a string"

    if type(first_name) != str:
        raise TypeError(e_1)
    if type(last_name) != str:
        raise TypeError(e_2)

    print("My name is {} {}".format(first_name, last_name))
