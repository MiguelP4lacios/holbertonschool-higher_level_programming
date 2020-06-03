#!/usr/bin/python3
"""Mudule
"""


def is_kind_of_class(obj, a_class):
        """Function

        Arguments:
            obj {[type]} -- [description]
            a_class {[type]} -- [description]

        Returns:
            [type] -- [description]
        """

        if isinstance(obj, a_class):
                return True
        else:
                return False
