#!/usr/bin/python3
"""A Rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialising the attributes
        args:
         width (int) : The width of the Rectangle
         height (int): The height of the Rectangle
         x(int): x coordinate
         y(int): y coordinate
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """width getter"""
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value

        @property
        def height(self):
            """width getter"""
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value

        @property
        def x(self):
            """width getter"""
            return self.__x

        @x.setter
        def x(self, value):
            
            self.__x = value

        @property
        def y(self):
            """width getter"""
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value
