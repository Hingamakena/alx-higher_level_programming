#!/usr/bin/python3
""" class Student defining a student """


class Student:
    """ instantiatin with the __init__ method """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    """ method to_json that retrieves a dictionary representation """

    def to_json(self, attrs=None):
        for i in range(0, len(attrs)):
            return i
        return self.__dict__
