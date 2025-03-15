#!/usr/bin/python3

""" from obj to json string"""


def to_json_string(my_obj):
    """ if main, import file json"""

    if __name__ == "__main__":
        import json
    """ return json obj dumping theonj"""

    return json.dumps(my_obj)
