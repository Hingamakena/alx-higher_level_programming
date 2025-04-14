#!/usr/bin/python3
""" imports a module from the base module file """
from models.base import Base

""" class rectangle inheriting from Base"""

class Rectangle(Base):

    """ class constructor """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ calls the super class with id """

        """ rest of the locally defined attributes """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """ inherit from super class id """

    """
    getter and setter excluding id """
