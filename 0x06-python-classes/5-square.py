#!/usr/bin/python3
""" class that defines a square"""


class Square:
    """ private instance size
        size method to set it """
    def __init__(self, size=0):
        self.__size = size
    """ getter method"""
    def size(self):
        return self.__size

    """setter method """
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size myst be an integer")
        if size < 0:
            raise ValueError("size myst be >= 0")
        self.__size = value

    """ returns the area of the square"""
    def area(self):
        return self.__size * self.__size

    """prints the square"""
    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("#")
