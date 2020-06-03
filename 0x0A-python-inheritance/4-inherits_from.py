#!/usr/bin/python3
"""Module
"""


def inherits_from(obj, a_class):
        """Function

        Arguments:
            obj {[type]} -- [description]
            a_class {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        if issubclass(type(obj), a_class) and type(obj) is not a_class:
                return True
        else:
                return False
