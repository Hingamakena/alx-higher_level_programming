#!/usr/bin/python3
""" add all unique integers in a list """

def uniq_add(my_list=[]):
    sum = 0
    for i in set(my_list):
        sum += i
    return sum
