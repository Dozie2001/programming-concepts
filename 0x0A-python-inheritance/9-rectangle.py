#!/usr/bin/python3
"""A folder that shows how inheritance works"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that shows how a rectangle works and inherits
    basic geometry properties from 'Base Geometry' """

    def __init__(self, width, height):
        """Initializes The rectangle class
        args:
        width (int): The width of a new rectangle
        height (int): The height of a new rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator('height', height)
        self.integer_validator('width', width)

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return The print representation and str representation of the Class"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
