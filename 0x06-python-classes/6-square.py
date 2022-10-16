#!/usr/bin/python3
"""Square Value"""


class Square:
    """
    Defines a Square and its basic properties
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """

    def __init__(self, size=0, position=(0, 0)):
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
        self.__position = position

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

    @property
    def position(self):
        """
        Retrieve the instance attribute position
        :return: the position (x, y)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        value == positive two value tuple
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif type(value[0] is not int) or type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integer")

    def area(self):

        """
        Calculates and returns the area of the square
        :return: the area of the square
        """

        return self.__size ** 2

    def my_print(self):
        """
        Print to the stdout '#' * size
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for line in range(self.__size):
                print(" " * self.__position[0], end='')
                print('#' * self.__size)
