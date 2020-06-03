#!/usr/bin/python3
"""[summary]

Raises:
    Exception: [description]
    TypeError: [description]
    ValueError: [description]
"""


class BaseGeometry():
    """Class
    """

    def area(self):
        """Method 1
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method 2

        Arguments:
            name {[type]} -- [description]
            value {[type]} -- [description]
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
