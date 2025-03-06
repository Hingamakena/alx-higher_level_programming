#!/usr/bin/python3

""" replace all occurences of an element by another in new list"""
def search_replace(my_list, search, replace):
    newlist = my_list[:]
    for i in newlist:
        if search == newlist[i]:
            newlist[search] = replace

    return newlist
