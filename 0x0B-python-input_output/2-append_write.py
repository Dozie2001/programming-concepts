#!/usr/bin/python3
"""A text-appending function that returns the number of bytes"""


def append_write(filename="", text=""):
    """
    appending a string to a UTF8

    args:
    filename(str): file to be appended to
    text(str): the text string to be appended to
    Returns:
      The number of string to be appended
    """

    with open(filename, "a", encoding='utf-8') as f:
        lines = f.write(text)

    return (lines)
