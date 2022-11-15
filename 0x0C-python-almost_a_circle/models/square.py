#!/usr/bin/python3
"""A SQUARE Class that inherits from A rectangle Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialises the Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.width = value
        self.height = value

    def __str__(self):
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
        """Update method"""
        if args is not None and len(args) != 0:
            list_args = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_args[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dict representation of the string"""
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            dict_res[key] = getattr(self, key)

        return dict_res
