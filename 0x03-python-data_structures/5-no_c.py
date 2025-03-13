#!/usr/bin/python3

def no_c(my_string):
    newstring = my_string[:]
    for i in len(my_string):
        if 'c' in my_string or 'C' in my_string:
            continue

    return my_string
