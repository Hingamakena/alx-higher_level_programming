#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ self instantiation with size=0, position =(0,0)"""
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

    """ getter of size """
    def size(self):
        return self.__size

    """ setter of size """
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    """ getter of position """
    def position(self):
        return self.__position

    """setter of position """
    def position(self, value):
        if not isinstance(value, tuple):
            raiseTypeError("position must be a tuple of 2 positive integers")

        self.__position = value
