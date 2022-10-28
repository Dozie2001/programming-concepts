#!/usr/bin/python3
"""A class that prevents the user from creating a new instance attribute"""


class LockedClass:
    """
    Prevents the user from creating a new instance """
    __slot__ = ["first_name"]

    def __init__(self):
        """Init Class """
        pass
