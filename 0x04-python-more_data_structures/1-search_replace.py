#!/usr/bin/python3

""" replace all occurences of an element by another in new list"""
def search_replace(my_list, search, replace):
    new_list = my_list[:]

    for i in range(0, len(new_list) - 1):
        if search in new_list:
            new_list[search] = replace
    return new_list
