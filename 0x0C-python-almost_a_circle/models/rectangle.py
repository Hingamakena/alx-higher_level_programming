#!/usr/bin/python3
from base import Base

""" class rectangle inheriting from Base"""

class Rectangle(Base):
    """ class constructor """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ calls the super class with id """

        super().id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
