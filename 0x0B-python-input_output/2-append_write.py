#!/usr/bin/python3
#2-append_write.py

"""append a string at the end of a text file"""

def append_write(filename="", text=""):
    """do that and return nb of characters added"""

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
