#!/usr/bin/python3
"""Module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
        """Class

        Arguments:
            BaseGeometry {[type]} -- [description]
        """

        def __init__(self, width, height):
                """Costructor

                Arguments:
                    width {[type]} -- [description]
                    height {[type]} -- [description]
                """
                BaseGeometry.integer_validator(self, "width", width)
                BaseGeometry.integer_validator(self, "height", height)
                self.__width = width
                self.__height = height

        def area(self):
                """Method 1

                Returns:
                    [type] -- [description]
                """
                return self.__width * self.__height

        def __str__(self):
                """Method 3

                Returns:
                    [type] -- [description]
                """
                return "[Rectangle] {}/{}".format(self.__width, self.__height)
