#!/usr/bin/python3

""" Check if object is anistance of the object """


def is_kind_of_class(obj, a_class):
    """ return true if obj is an instance | inherited from
    specified class """

    if isinstance(obj, a_class):
        return True
    else:
        return False
