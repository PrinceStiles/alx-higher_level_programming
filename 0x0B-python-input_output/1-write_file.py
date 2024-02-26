#!/usr/bin/python3
# 1-write_file.py

"""write a string to a text file"""


def write_file(filename="", text=""):
    """do that and return nb of characters"""

    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
