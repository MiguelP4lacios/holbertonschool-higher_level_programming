#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""3-square.py

This module contains an class

A class that defines a square by:
-Private instance attribute: size
-Instantiation with size(optional):
            def __init__(self, size=0, position=(0, 0))
"""


class Square:
    """
    This is an class Square that defines a square

    Attributes:
        __size (int): The size of square
        size must be an integer that is 0 or greater
        position (tuple) : The position of squere
        must be a tuple of 2 positive integers.
    """
    def __init__(self, size=0, position=(0, 0)):
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
        if type(position) != tuple or len(position) != 2:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        elif type(position[0]) != int or type(position[1]) != int:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        elif position[0] < 0 or position[1] < 0:
            print("position must be a tuple of 2 positive integers", end="")
            raise TypeError
        else:
            self.__position = position

    def area(self):
        """
        This function calculates the area of a square

         Returns:
            Square: The area of a square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        This property is to get it back
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        This property is to configure it
        """
        self.__size = value

    @property
    def position(self):
        """
        This property is to get it back
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        This property is to configure it
        """
        self.__position = value

    def my_print(self):
        """
        This function prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for erow in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for sp in range(self.position[0]):
                    print(" ", end="")
                for c in range(self.__size):
                    print("#", end="")
                print()
