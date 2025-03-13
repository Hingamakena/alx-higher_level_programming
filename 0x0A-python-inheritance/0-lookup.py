#!/usr/bin/python3

""" A function that returns list of available attributes
    and methods of an object """
def lookup(obj):
    try:
        return dir(obj)
    except Error as e:
        print(e)
