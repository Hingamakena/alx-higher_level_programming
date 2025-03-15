#!/usr/bin/python3

def write_file(filename="", text=""):
    """writes a string to text file and return no of chars"""
    with open(filename, "rw") as f:
        f.read(filename)
        f.write(text, filename)
