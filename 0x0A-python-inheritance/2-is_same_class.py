#!/usr/bin/python3

""" check if an obj is an instance of the specified class """


def is_same_class(obj, a_class):
    """ if isinstance return True, else False"""

    if isinstance(obj, a_class.__class__):
        return True
    else:
        return False
