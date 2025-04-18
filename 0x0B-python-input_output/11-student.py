#!/usr/bin/python3
""" importing json module """
import json

class Student:
    """ instantiation with public instance attrs """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        return self.__dict__

    def reload_from_json(self, json):
        return json.loads(json)
