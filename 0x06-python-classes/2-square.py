#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""2-square.py

This module contains an class

A class that defines a square by:
-Private instance attribute: size
-Instantiation with size(optional): def __init__(self, size=0)
"""


class Square:
    """
    This is an class Square that defines a square

    Attributes:
        __size (int): The size of square
        size must be an integer that is 0 or greater
    """
    def __init__(self, size=0):
        """
        The constructor for Square class.

        Parameters:
            size (int): The size of square.
        """
        if type(size) != int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
