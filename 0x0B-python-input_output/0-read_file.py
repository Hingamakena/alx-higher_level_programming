#!/usr/bin/python3

""" read a text and prints it to stdout"""


def read_file(filename=""):
    """ using with so as to automatically close the file"""

    with open(filename, "r", encoding="utf-8") as f:
        data = f.read()
    print(data, end="")
