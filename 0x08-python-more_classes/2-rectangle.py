#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains an class that defines a rectangle.
"""


class Rectangle:
    """class Rectangle that defines a rectangle
    """
    __erro_1 = "width must be an integer"
    __erro_2 = "height must be >= 0"

    def __init__(self, width=0, height=0):
        """construtor
        """
        if type(width) != int:
            raise TypeError(Rectangle.__erro_1)
        elif width < 0:
            raise ValueError(Rectangle.__erro_2)
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError(Rectangle.__erro_1)
        elif width < 0:
            raise ValueError(Rectangle.__erro_2)
        else:
            self.__height = height

    @property
    def height(self):
        """getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter
        """
        if type(value) != int:
            raise TypeError(Rectangle.__erro_1)
        elif value < 0:
            raise ValueError(Rectangle.__erro_2)
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
            raise TypeError(Rectangle.__erro_1)
        elif value < 0:
            raise ValueError(Rectangle.__erro_2)
        else:
            self.__width = value

    def area(self):
        """This function renturn the area
        """
        return self.__width * self.__height

    def perimeter(self):
        """This function return the perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
