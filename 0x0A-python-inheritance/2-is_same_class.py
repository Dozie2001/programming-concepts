#!/usr/bin/python3
""" A function that checks if isninstance of a class"""


def is_same_class(obj, a_class):
    """The funstion that checks if a class is the same as the object"""
    if type(obj) is a_class:
        return True
    else:
        return False
