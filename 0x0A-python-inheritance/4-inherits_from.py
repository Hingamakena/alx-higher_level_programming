#!/usr/bin/python3

""" check if obj isinstance of an inherited class """


def inherits_from(obj, a_class):
    """ if a subclass return True, else, False"""

    if isinstance(obj, a_class):
        if type(obj) is not a_class:
            return True
    else:
        return False
