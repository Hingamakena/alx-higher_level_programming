#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    newlist = my_list[:]
    for i in range(len(newlist)):
        if my_list[idx] > len(my_list):
            return new_list
        if my_list[idx] < 0:
            return newlist

    newlist[idx] = element

    return newlist
