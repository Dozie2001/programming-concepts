#!/usr/bin/python3
"""A function that defines a Class-To-JSON"""


def class_to_json(obj):
    """Returns dictionary representation of simple data Structure"""
    return obj.__dict__
