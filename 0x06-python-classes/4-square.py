#!/usr/bin/python3

""" class Square that defines a square """


class Square:
    """ instantiation with __init__ """
    def __init__(self, size=0):
        self.__size = size

    """ getter of the __self"""
    @property
    def size(self):
        return self.__size
    
    """ setter of size variable"""
    @size.setter
    def size(self, value):
        self.__size = value

    """ return size sqared """
    def area(self):
        return self.__size * self.__size
