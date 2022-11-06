#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a Square in BaseGeometry"""

    def __init__(self, size):
        """Initializes the Square class
        args:
        size(int): The size of an intg"""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)
