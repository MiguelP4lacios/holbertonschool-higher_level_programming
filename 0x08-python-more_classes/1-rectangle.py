#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains an class that defines a rectangle.
"""


class Rectangle:
    """class Rectangle that defines a rectangle
    """
    __erro_1 = "must be an integer"
    __erro_2 = "must be >= 0"

    def __init__(self, width=0, height=0):
        """construtor
        """
        if type(width) != int:
            raise TypeError("width "+Rectangle.__erro_1)
        elif width < 0:
            raise ValueError("width "+Rectangle.__erro_2)
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height "+Rectangle.__erro_1)
        elif width < 0:
            raise ValueError("height "+Rectangle.__erro_2)
        else:
            self.__height = height

    @property
    def height(self):
        """Getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter
        """

        if type(value) != int:
            raise TypeError("height "+Rectangle.__erro_1)
        elif value < 0:
            raise ValueError("height "+Rectangle.__erro_2)
        else:
            self.__height = value

    @property
    def width(self):
        """getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter
        """
        if type(value) != int:
            raise TypeError("width "+Rectangle.__erro_1)
        elif value < 0:
            raise ValueError("width "+Rectangle.__erro_2)
        else:
            self.__width = value
