#!/usr/bin/python3
"""Module convert class to JSON
"""


def class_to_json(obj):
        """Function → class to JSON

        Args:
            obj ([type]): object

        Returns:
            [type]: dict
        """
        return obj.__dict__
