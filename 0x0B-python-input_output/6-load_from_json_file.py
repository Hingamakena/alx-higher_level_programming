#!/usr/bin/python3

""" import the json module """
import json 

""" load from json file """
def load_from_json_file(filename):
    """ using open with with to read file """

    with open(filename, encoding="utf-8") as my_file:
        """ read my file """
        read_data = my_file.read()
        my_data = json.loads(read_data)

        """ return loaded json data """
        return my_data
