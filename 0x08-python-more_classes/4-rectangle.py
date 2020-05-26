#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains an class that defines a rectangle.
"""


class Rectangle:
    """class Rectangle that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """construtor
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("height must be >= 0")
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
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
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
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
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

    def __str__(self):
        """print the rectangle with the character #
        """
        rectg = ""
        if self.__width == 0 or self.__height == 0:
            return rectg
        for h in range(self.__height - 1):
            rectg += ("#" * self.__width) + "\n"
        rectg += ("#" * self.__width)
        return rectg

    def __repr__(self):
        """Return a string representation of the rectangle
            to be able to recreate
        """
        return 'Rectangle({self.width}, {self.height})'.format(self=self)
