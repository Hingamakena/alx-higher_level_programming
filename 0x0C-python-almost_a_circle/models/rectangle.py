#!/usr/bin/python3
from base import Base

""" class Rectangle inherits from Base class """


class Rectangle(Base):

    """ Base class inherited from module base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ id is inherited from the baseclass
            width a property of instance
            height - a property of instance
            id - an inherited property of instance
        """
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """ height getter """
        return self.__height

    @property
    def width(self):
        """ width getter """
        return self.__width

    @height.setter
    def height(self, value):
        """ height property setter """
        if not isinstance(value, int):
            print("value is not an integer")

        self.__height = value
    
    @width.setter
    def width(self, value):
        """ Width property setter """
        if not isinstance(value, int):
            print("value is not an integer")

        self.__width = value
