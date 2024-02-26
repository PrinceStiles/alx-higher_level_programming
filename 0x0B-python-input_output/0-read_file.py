#!/usr/bin/python3

"""function that reads a file and prints it to stdout"""

def read_file(filename=""):
    """print the contents of a UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
