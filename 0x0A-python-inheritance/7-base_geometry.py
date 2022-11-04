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

    def integer_validator(self, name, value):
        """Validates values
        args:
        name (str): Name of value
        value (int): Value to be validated

        Raises:
        TypeError: If value is not an integer
        ValueError: If value is not greater than or equal to 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
