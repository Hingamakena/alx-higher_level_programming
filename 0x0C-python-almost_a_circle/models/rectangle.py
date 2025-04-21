#!/usr/bin/python3
""" imports a module from the base module file """
from models.base import Base

""" class rectangle inheriting from Base"""


class Rectangle(Base):

    """ class constructor with attributes width, height, x, y """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    """
    getter and setter excluding id """

    """ method area returning the area of the rectangle """
    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(0, self.__height):
            for j in range(0,self.__width):
                print('#',end="")
            print('#')
    """ return the string rep of the class """
    def __str__(self):
        return f"{self.__class__.__name__} ({self.id}) {self.__x}/{self.__y} {self.__width}/{self.__height}"
