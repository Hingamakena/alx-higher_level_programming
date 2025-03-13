#!/usr/bin/python3

""" A function that returns list of available attributes
    and methods of an object """


def lookup(obj):
    """ using a try block to print dir of the object """

    try:
        return dir(obj)
    except Error as e:
        print(e)
