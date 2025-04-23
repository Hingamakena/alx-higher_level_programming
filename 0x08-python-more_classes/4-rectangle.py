#!/usr/bin/python3

""" class REctangle that defines a rectangle"""


class Rectangle:
    """ instantiation with optional width and height """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """ retrieve width """
    @property
    def width(self):
        return self.__width

    """ retrieve the height property """
    @property
    def height(self):
        return self.__height
    
    """ set the width property """
    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    """ set the height property with the value """
    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    """return the area of the rectangle"""
    def area(self):
        return (self.__height * self.__width)

    """ return the perimeter of the rectangle """
    def perimeter(self):
        if self.__height == 0 and self.__width == 0:
            return (0)
        return ((self.__height + self.__width) * 2)
