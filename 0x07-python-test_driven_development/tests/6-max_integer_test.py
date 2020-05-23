#!/usr/bin/python3
"""Mudule test
"""

import unittest

max_integer = __import__('6-max_integer').max_integer

class testing_max_integer(unittest.TestCase):
    """Class test

    Arguments:
        unittest {[type]} -- [description]
    """
    def test_1(self):
        """test_1
        """
        self.assertAlmostEquals(max_integer([1,2,5,4]), 5)


