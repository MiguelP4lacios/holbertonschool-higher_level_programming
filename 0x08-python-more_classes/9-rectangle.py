#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module contains an class that defines a rectangle.
"""


class Rectangle:
    """class Rectangle that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

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
        """print the rectangle with the character any simb
        """
        rectg = ""
        if self.__width == 0 or self.__height == 0:
            return rectg
        for h in range(self.__height - 1):
            rectg += (str(self.print_symbol) * self.__width) + "\n"
        rectg += (str(self.print_symbol) * self.__width)
        return rectg

    def __repr__(self):
        """Return a string representation of the rectangle
            to be able to recreate
        """
        return '{self.__class__.__name__}\
            ({self.width}, {self.height})'.format(self=self)

    def __del__(self):
        """Print the message at delete
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances += -1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Class method that returns a square
        """
        return Rectangle(width=size, height=size)
