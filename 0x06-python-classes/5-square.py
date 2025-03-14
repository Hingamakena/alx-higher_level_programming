#!/usr/bin/python3

class Square:
    """ private instance size
        size method to set it """
    def __init__(self, size=0):
        self.__size = size

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size myst be an integer")
        if size < 0:
            raise ValueError("size myst be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("#")
