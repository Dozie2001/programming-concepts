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
        return self.__width

    @size.setter
    def size(self, value):
        """ Setter size """
        self.__width = value
        self.__height = value
