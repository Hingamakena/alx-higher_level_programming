#!/usr/bin/python3
""" class Rectangle that defines a rectangle """


class Rectangle:
    """ instantiation with optional width and height """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """ getter method of width """
    def width(self):
        return self.__width

    """ setter method width"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    """ getter method height """
    def height(self):
        return self.__height

    """ setter method height """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    """ method area"""
    def area(self):
        return (self.__width * self.__height)

    """ method perimeter """
    def perimeter(self):
        return ((self.__width + self.__height) * 2 )
