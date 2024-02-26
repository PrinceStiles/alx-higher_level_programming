#!/usr/bin/python3
#1-write_file.py

"""Function to write a text to a file"""

def write_file(filename="", text=""):
    """write string to text file and
    return number of characters"""
    
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
