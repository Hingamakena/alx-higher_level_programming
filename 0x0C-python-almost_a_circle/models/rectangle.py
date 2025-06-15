#!/usr/bin/python3

""" import Base Class from the base module """

from models.base import Base

""" class Rectangle inherits from Base class """


class Rectangle(Base):

    """ Rectangle class inherits from Base
        Represents a rectangle with x and y positions
        Rectangle dimensions are represented with height and witdh
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance

        Args:
            width (int): Width of rectangle (must be > 0)
            height (int): height of rectangle (must be > 0)
            x (int, optional):x co-ordinate (must be >= 0)
            y (int): y-coordinate(must be >= 0)

        Raises:
            TypeError: if any attribute is not an integer
            ValueError: if width or height less than 0
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ getter of height """
    @property
    def height(self):
        return self.__height

    """ getter of width property """
    @property
    def width(self):
        """ width getter """
        return self.__width

    """ getter of x property """
    @property
    def x(self):
        """ x property setter """
        return self.__x

    """ getter of y property """
    @property
    def y(self):
        """ y property setter """
        return self.__y

    """ height property setter """
    @height.setter
    def height(self, value):
        """ height property setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")

        self.__height = value

    """ setter of the width property """
    @width.setter
    def width(self, value):
        """ Width property setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    """ setter of the x property """
    @x.setter
    def x(self, value):
        """ setter property of x attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    """ setter of Y property """
    @y.setter
    def y(self, value):
        """ setter property of y attribute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
