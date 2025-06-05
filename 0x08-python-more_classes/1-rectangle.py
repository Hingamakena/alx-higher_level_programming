#!/usr/bin/python3

""" Defines a Rectangle class with width and height attributes """

class Rectangle:

    """ Rectangle class with width and height properties """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width of the rectangle """
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieve the height of the rectangle """
        return self.__height


    @height.setter
    def height(self, value):
        """ set the height of the rectangle """
        if not isinstance(self, value):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
        self.__height = value
