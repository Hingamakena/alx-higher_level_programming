#!/usr/bin/python3
import json

""" saves a json object in a file"""


def save_to_json_file(my_obj, filename):
    """ opens a file with name filename """

    with open(filename, encoding="utf-8") as f:
        write_data = f.write(json.dumps(my_obj))

    return write_data
