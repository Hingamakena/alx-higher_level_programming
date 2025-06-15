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

    @property
    def x(self):
        """ x property setter """
        return self.__x

    @property
    def y(self):
        """ y property setter """
        return self.__y

    @height.setter
    def height(self, value):
        """ height property setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")

        self.__height = value
    
    @width.setter
    def width(self, value):
        """ Width property setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """ setter property of x attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """ setter property of y attribute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
