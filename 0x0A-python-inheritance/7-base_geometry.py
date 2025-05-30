#!/usr/bin/python3

""" class base Geometry with """


class BaseGeometry:
    """ public instance method area that raises an exception """

    def area(self):
        raise Exception("area() is not implemented")

    """ public instance method that validates value """

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        self.name = name
        self. value = value
