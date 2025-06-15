#!/usr/bin/python3
from base import Base
""" class Rectangle inherits from Base """


class Rectangle(Base):
    """ width - width of the class
        height - hwight of the class
        x and y instances
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)

        """ id is inherited from the baseclass """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            print("value is not an integer")

        self.__height = value
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            print("value is not an integer")

        self.__width = value
