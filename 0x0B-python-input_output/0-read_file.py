#!/usr/bin/python3

def read_file(filename=""):
    """ reads a test file(utf*) mode and print to stdout"""

    with open(filename, "r") as f:
        f.read(filename)
