#!/usr/bin/python3

""" function appends into a filename the text"""


def append_write(filename="", text=""):
    """ using with to open filename """

    with open(filename, 'a', encoding="utf-8") as f:
       mydata =  f.write(text)

    return mydata
