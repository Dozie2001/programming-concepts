#!/usr/bin/python3
"""A class that Inherits from int"""


class MyInt():
    """Invert int operators == and !="""
    def __init__(self, value=0):
        self.value = value

    def __eq__(self, other):
        """Returns != instead of =="""
        return self.value != other

    def __ne__(self, other):
        """Returns == instead of !="""
        return self.value == other
    
    def __str__(self):
        return str(self.value)
