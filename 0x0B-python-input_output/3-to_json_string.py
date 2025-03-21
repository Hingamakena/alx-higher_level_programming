#!/usr/bin/python3

""" from obj to json string"""
import json
""" from my_obj to json"""


def to_json_string(my_obj):
    """return obj dumped to json """

    return json.dumps(my_obj)
