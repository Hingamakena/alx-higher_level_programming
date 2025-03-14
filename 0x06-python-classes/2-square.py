#!/usr/bin/python3
""" class square defining a square"""


class Square:
    """private instance size
        size must be an integer"""

    def __init__(self, size=0):
        self.__size = size
        try:
            isinstance(size, int)
        except TypeError:
            print("size must be an integer")
        try:
            int(size) > 0
        except ValueError:
            print("size must be >= 0")
