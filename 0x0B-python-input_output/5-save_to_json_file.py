#!/usr/bin/python3

""" imports a son module """
import json

""" saves a json object in a file"""

def save_to_json_file(my_obj, filename):

    """ opens a file with name filename """

    with open(filename="", encoding="utf-8") as f:
        read_file = f.read()
        write_file = f.write(json.dumps(my_obj))

    """ returns written data holder"""
    return write_file
