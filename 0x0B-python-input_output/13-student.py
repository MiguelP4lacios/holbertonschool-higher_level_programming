#!/usr/bin/python3
"""Module
"""


class Student:
    """Class
    """
    def __init__(self, first_name, last_name, age):
        """Constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method
        """
        if type(attrs) is list:
            aux_dict = {}
            for x in attrs:
                if type(x) is str and x in self.__dict__.keys():
                    aux_dict[x] = self.__dict__.get(x)
            return aux_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """[summary]

        Args:
            json ([type]): dict
        """
        alist_keys = list(json.keys())
        for key in alist_keys:
            self.__dict__[key] = json.get(key)
