#!/usr/bin/python3

""" deletes an item at a specific positio  in list """


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return None
    my_list.pop(idx)
    return my_list
