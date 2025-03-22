#!/usr/bin/python

def max_integer(my_list=[]):
    x = 0
    for i in range(0, len(my_list)):
        if my_list[i] > my_list[i+1]:
            x = my_list[i]
        else:
            x = my_list[i+1]

    return x
