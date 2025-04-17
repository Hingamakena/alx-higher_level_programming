#!/usr/bin/python3

def no_c(my_string):
    new_string = list(my_string)
    for i in range(0, len(new_string)):
        if 'c' in new_string:
            new_string.remove(i)
        if 'C' in new_string:
            new_string.remove(i)
    return str(new_string)
