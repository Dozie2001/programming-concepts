#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None
    key_tuple = tuple(a_dictionary.keys())
    for key in key_tuple:
        if value == a_dictionary[key]:
            del a_dictionary[key]
    return a_dictionary
