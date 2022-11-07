#!/usr/bin/python3
"""A Function that reads  FILE"""


def read_file(filename=""):
    """args
    @filename: file to be read
    """
    with open(filename, encoding="utf-8") as f:
        lines = f.read

    print(lines, end='')
