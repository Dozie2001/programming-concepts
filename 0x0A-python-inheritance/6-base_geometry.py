#!/usr/bin/python3
"""A Base Geometry"""


class BaseGeometry:
    """A Class that functions for basic geometry"""

    def __init__(self):
        """Initialising an empty attribute"""
        pass

    def area(self):
        """Calculates the area of a shape"""
        raise Exception("area() is not implemented")
