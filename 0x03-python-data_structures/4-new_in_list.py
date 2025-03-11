#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    newlist = my_list[:]

    if idx >= len(my_list):
        return my_list
    if idx < 0:
        return newlist

    newlist[idx] = element

    return newlist
