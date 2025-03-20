#!/usr/bin/python3

""" check if obj isinstance of an inherited class """


def inherits_from(obj, a_class):
    """ if a subclass return True, else, False"""

    if issubclass(obj, a_class):
        return True
    else:
        return False
