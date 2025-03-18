#!/usr/bin/python3

""" replace all occurences of an element by another in new list"""
def search_replace(my_list, search, replace):
    newlist = my_list[:]

    for i in range(0, len(my_list)):
        if search in my_list:
            newlist[search] = replace
    return newlist
