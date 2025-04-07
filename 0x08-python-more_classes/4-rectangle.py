#!/usr/bin/python3
""" class defines a rectabgle """


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
    """ property to retrieve width """
    def width(self):
        return self.__width

    """ propeerty setter of width """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__height * self.__width

    def repr():
        return  f"self.__dict__.__str__"

    def perimeter(self):
        return ((self.__height * 2) + (self.__width * 2))
