#!/usr/bin/python3

""" read file, filename as argument"""


def read_file(filename=""):
    """ reads a test file(utf*) mode and print to stdout"""

    with open(filename,  encoding="utf-8") as file_handler:
        read_data = file_handler.read()
        print("{}".format(read_data))

        return read_data
