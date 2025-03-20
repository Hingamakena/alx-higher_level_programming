#!/usr/bin/python3

""" class BaseGeometry with public instance method that raises
    Exception with message """


class BaseGeometry:
    """ public method area"""

    def area(self):
        raise Exception("area() is not implemented")
