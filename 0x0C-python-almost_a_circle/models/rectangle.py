#!/usr/bin/python3
""" imports a module from the base module file """
from models.base import Base

""" class rectangle inheriting from Base"""


class Rectangle(Base):

    """ class constructor with the class trributes 
    calls the super class with id using the logic of __init__"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
