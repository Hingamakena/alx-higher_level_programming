#!/usr/bin/python3

"""return a list qith all values multiplied by number with no loop"""


def multiply_list_map(my_list=[], number=0):
    newlist = list(map(lambda x: (x * number), my_list))
    return newlist
