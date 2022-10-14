#!/usr/bin/python3
"""A Class that is meant to function Like a Square"""


class Square:
    """
    Defines a Square and its basic properties
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """

    def __init__(self, size):
        self.__size = size
