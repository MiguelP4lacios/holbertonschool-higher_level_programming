#!/usr/bin/python3"
"""Module that comvert str a object

Returns:
        [type]: object
"""


import json


def from_json_string(my_str):
        """[summary]

        Args:
            my_str ([type]): str_object

        """
        return json.loads(my_str)
