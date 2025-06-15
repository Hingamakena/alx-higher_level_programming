#!/usr/bin/python3

""" class Rectangle inherits from Base """


class Rectangle(Base):
    """ width - width of the class
        height - hwight of the class
        x and y instances
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
