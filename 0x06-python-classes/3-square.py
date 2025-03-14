#!/usr/bin/python3

""" class square that defines a square """


class Square:
    """ private instance size """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        """ defines the area of the square """
        self.__size = size

    def area(self):
        return self.__size * self.__size
