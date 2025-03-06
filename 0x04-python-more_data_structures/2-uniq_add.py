#!/usr/bin/python3

""" function that adds all unique integers in list """
def uniq_add(my_list=[]):
    count = 0
    for i in len(my_list):
        if my_list[i] != my_list[i + 1]:
            count += i

    return count
