#!/usr/bin/python3
""" class defines a rectabgle """


class Rectangle:
    self.__width=0
    
    """ property to retrieve width """
    def width(self):
        return self.__width

    """ propeerty setter of width """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("must be an integer")
