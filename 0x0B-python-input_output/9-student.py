#!/usr/bin/python3
""" class Student defining a student """

class Student:
    """ instantiation with first_name and last_name """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name= last_name
        self.age = age
    """ method retrieves a dictionary representatin of a student """

    def to_json(self):
        return self.__dict__
