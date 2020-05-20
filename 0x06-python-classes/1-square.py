#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""1-square.py

This module contains an class

A class that defines a square by:
-Private instance attribute: size
-Instantiation with size (no type/value verification)
"""


class Square:
    """
    This is an class Square that defines a square

    Attributes:
        __size (any): The size of square
    """
    def __init__(self, size):
        """
        The constructor for Square class.

        Parameters:
            size (int): The size of square.
        """
        self.__size = size
