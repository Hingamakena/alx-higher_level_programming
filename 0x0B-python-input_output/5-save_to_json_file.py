#!/usr/bin/python3
""" import json module """
import json

""" function writes obj to text file in JOSN """


def save_to_json_file(my_obj, filename):
    """ write obj to text file """
    data = json.dumps(my_obj)

    with open(filename, encoding="utf-8") as f:
        data_written = f.write(data)

    return data_written
