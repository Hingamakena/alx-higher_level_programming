#!/usr/bin/python3

""" class rectangle with height and width """


class Rectangle:

    """ private instances """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ width getter """
    @property
    def width(self):
        return self.width
    
    """ property width setter """
    @width.setter
    def width(self, value):
        if not isinstance(int, value):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.width = value

    """ property height getter """
    @property
    def height(self):
        """ height getter method """
        return self.height

    """ property height setter """
    @height.setter
    """ height setter method """
    def height(self, value):
        if not isinstance(self, value):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
        self.height = value
