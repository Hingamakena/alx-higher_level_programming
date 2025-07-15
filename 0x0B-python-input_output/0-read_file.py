#!/usr/bin/python3

""" reads a file and prints the data read """


def read_file(filename=""):
    """ using with to automatically open and close file """

    with open(filename, "r") as reading_file:
        the_read_file = reading_file.read()
        print(the_read_file)
