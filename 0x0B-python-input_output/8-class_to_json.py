#!/usr/bin/python3
""" function returns dict description with a simple data list"""


def class_to_json(obj):

    """ returns a dictionary obj of the obj file """
    return obj.__dict__
