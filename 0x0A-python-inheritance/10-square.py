#!/usr/bin/python3
"""Module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
        """Class

        Arguments:
            Rectangle {[type]} -- [description]
        """
        def __init__(self, size):
                self.integer_validator("size", size)
                self.__size = size
                self._Rectangle__width = size
                self._Rectangle__height = size

        def area(self):
                """Method

                Returns:
                    [type] -- [description]
                """
                return self.__size**2
