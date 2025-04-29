#!/usr/bin/python3

""" read a text and prints it to stdout"""


def read_file(filename=""):
    with open(filename, "r") as f:
        data = f.read()
    print(data, end="")
