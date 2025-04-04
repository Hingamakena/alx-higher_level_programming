#!/usr/bin/python3

""" class Rectangle with height and width """

class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("Width must be an integer")

        if width < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return ((self.__width * 2) + (self.__height * 2))
