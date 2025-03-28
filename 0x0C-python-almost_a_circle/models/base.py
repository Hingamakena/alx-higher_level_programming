#!/usr/bin/python3

""" first class Base """


class Base:

    """ private attribute of class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            self.id = id
        else:
            Base.__nb_bojects += 1
            self.id = Base._nb_objects

if __name__ == "__main__":
    import doctest
    doctest.testfile("test_base.txt")
