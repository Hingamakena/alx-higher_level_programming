#!/usr/bin/python3

""" Class Base the base class of all other classes """
class Base:
    """ private attribute """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
