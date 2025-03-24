#!/usr/bin/python3

""" class Square that defines a square """


class Square:
    """ instantiation with size """

    def __init__(self, size=0):
        self.__size = size

    """ getter of size """
    def size(self):
        return self.__size

    """ setter of size """
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    """ return size sqared """
    def area(self):
        return self.__size__ * self.__size__
