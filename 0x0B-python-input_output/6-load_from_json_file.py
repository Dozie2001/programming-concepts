#!/usr/bin/python3
"""A function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Uses json load to create a Python Object"""
    with open(filename) as f:
        return json.load(f)
