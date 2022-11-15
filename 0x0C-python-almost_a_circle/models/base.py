#!/usr/bin/python3
"""A class that will be the base of all our other classes"""
import json


class Base:
    """A class that will manage all our other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialising the class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string representation"""
        if list_dictionaries is None or list_dictionaries == '[]':
            return "[]"
        return json.dumps(list_dictionaries)
