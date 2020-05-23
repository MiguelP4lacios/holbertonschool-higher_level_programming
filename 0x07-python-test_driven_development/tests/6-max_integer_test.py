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
    def test_middle(self):
        """test_middle
        """
        self.assertAlmostEquals(max_integer([1,2,5,4]), 5)

    def test_end(self):
        """test_middle
        """
        self.assertAlmostEquals(max_integer([1,2,4,5]), 5)

    def test_beginning(self):
        """test_middle
        """
        self.assertAlmostEquals(max_integer([5,2,4,2]), 5)

    def test_only_negative_numbers(self):
        """test_middle
        """
        self.assertAlmostEquals(max_integer([-1,-3,-100,-4]), -1)

    def test_one_negative_number(self):
        """test_middle
        """
        self.assertAlmostEquals(max_integer([-100]), -100)

    def test_one_number(self):
        """test_middle
        """
        self.assertAlmostEquals(max_integer([100]), 100)

    def test_empty(self):
        """test_middle
        """
        self.assertFalse(max_integer([]))
