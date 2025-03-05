#!/usr/bin/python3

class Square:
    """ class Square defining a square"""
    def __init__(self, size=0):
        self.__size = size

        if size is not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
