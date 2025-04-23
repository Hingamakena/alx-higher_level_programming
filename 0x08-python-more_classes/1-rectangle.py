#!/usr/bin/python3

""" class Rectangle that defines a rectangle on width and height"""


class Rectangle:
    """ instantiation with optional width and height """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """ retrieve the width value """
    @property
    def width(self):
        return self.__width

    """ set the value of width """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be bean integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ retrieve the height value """
    @property
    def height(self):
        return self.__height

    """ property setter of height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
