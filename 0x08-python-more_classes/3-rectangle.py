#!/usr/bin/python3
""" simple class Rectangle """


class Rectangle:
    """ instantiation fo the class attributes """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """ set width value """
    def width(self, value):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")

        if self.__width < 0:
            raise ValueError("width must be >= 0")

   
