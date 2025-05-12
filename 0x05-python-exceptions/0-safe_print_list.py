#!/usr/bin/python3

""" print x elements of a list """
def safe_print_list(my_list=[], x=0):
    """ loop through list and print x elements """
    try:
        for i in range(0, x):
            print(my_list[i])
    except Exception as e:
        return None
