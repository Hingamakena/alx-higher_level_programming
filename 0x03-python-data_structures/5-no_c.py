#!/usr/bin/python3

def no_c(my_string):
    for i in my_string:
        if 'c' in my_string:
            my_string[i] = 'f'
        i += 1
    return my_string
