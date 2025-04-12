#!/usr/bin/python3

""" write into a file, the filename and text as arguments"""


def write_file(filename="", text=""):
    """writes a string to text file and return no of chars

        using with to read and write data"""

    with open(filename, 'r+', encoding="utf-8") as f:
        written_data = f.write(text)

        return written_data
        
