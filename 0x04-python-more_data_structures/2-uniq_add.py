#!/usr/bin/python3
""" add all unique integers in a list """

def uniq_add(my_list=[]):
    for i in range(len(my_list)):
        for j in range(len(my_list[:])):
            if i != j:
                sum = +1

