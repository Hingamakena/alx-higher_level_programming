#!/usr/bin/python3

""" function that adds all unique integers in list """


def uniq_add(my_list=[]):
    """ function adds all unique integers in list"""
    count = 0

    newlist = set(my_list)
    list2 = list(newlist)

    for i in range(0, len(list2)):
        count += list2[i]
    return count
