#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.__position = position

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def position(self):
        return self.__position

    def position(self, value):
        if not isinstance(value, tuple):
            raiseTypeError("position must be a tuple of 2 positive integers")

        self.__position = value
