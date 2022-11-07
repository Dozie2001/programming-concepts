#!/usr/bin/python3
"""a function that writes an Object to a text file usig JSON"""
import json


def save_to_json_file(my_obj, filename):
    """"Write an object to a text file using JSON representation.
    args:
     filename: FILE to be written to
     my_obj: object to be represented"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
