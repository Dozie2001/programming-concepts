#!/usr/bin/python3
"""A text inserting Function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a particular text after each line
    args:
     filename(str): The filename
     search_string(str): Where text searching will start from
     new_string(str): The string to be added"""

    text = ""

    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)
