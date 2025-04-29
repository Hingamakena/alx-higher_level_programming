#!/usr/bin/python3

""" function writes a string to text file """


def write_file(filename="", text=""):
    """ using with for automated file closing """

    with open(filename, "w", encoding="utf-8") as f:
        data_written = f.write(text)

    return data_written
