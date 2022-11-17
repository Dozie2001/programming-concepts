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

    @classmethod
    def save_to_file(cls, list_objs):
        """Updating the class Base"""
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        empty_list = []
        if not json_string:
            return empty_list
        json.loads(json_string)
