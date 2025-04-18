#!/usr/bin/python3

"""updated class Rectangle"""


class Rectangle:
    """ initialization with height and width as private """

    def __init__(self, height=0, width=0):
        self.__width = width
        self.__height = height

    """ property getter of width"""
    @property
    def width(self):
        return self.__width

    """ property setter of width """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an int")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    """ property getter of height """
    @property
    def height(self):
        return self.__height

    """ property setter of height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an int")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
