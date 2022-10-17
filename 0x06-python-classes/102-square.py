#!/usr/bin/python3
"""Square Value"""


class Square:
    """
    Defines a Square and its basic properties
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """

    def __init__(self, size=0):
        """
        Innitialize the size of the square. the size can be specified.
        If they are not, the size defaults to 0
        :param size: int size of square ( > 0)
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Set the value of the size
        :param: int size
        """

        return self.__size

    @size.setter
    def size(self, value):

        """
        Set the value of the size
        :param: int size
        """

        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):

        """
        Calculates and returns the area of the square
        :return: the area of the square
        """

        return self.__size ** 2

    def __eq__(self, other):
        """Returns True if the area of the attribute is equal to the other"""

        return self.area() == other.area()

    def __ne__(self, other):
        """Defining the != to the area of the Square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defining < to the area of the Square"""
        return self.area() < other.area()

    def __gt__(self, other):
        """Defining > than the area of the Square"""
        return self.area() > other.area()

    def __le__(self, other):
        """Defining <= to the area of the Square"""
        return self.area() <= other.area()

    def __ge__(self, other):
        """Defining >= tot the are of the Square"""
        return self.area() >= other.area()
