#!/usr/bin/python3
"""A class that will be the base of all our other classes"""

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
