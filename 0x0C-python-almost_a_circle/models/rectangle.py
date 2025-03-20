#!/usr/bin/python3
from base import Base

""" class rectangle inheriting from Base"""


class Rectangle(Base):
    pass


if __name__ == "__main__":
    import doctest
    doctest.testfile("test_rectangle.txt")
