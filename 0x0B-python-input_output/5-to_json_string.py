#!/usr/bin/python3
"""Module that convert to JSON_string
"""


import json


def to_json_string(my_obj):
        """Function that Serialize obj to a JSON formatted str

        Args:
            my_obj ([type]): object

        Returns:
            [type]: str
        """
        return json.dumps(my_obj)
