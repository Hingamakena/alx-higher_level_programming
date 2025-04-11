#!/usr/bin/python3
""" import json module """
import json


def from_json_string(my_str):
    """ return an obj of python data structure"""

    return json.loads(my_str)
