#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """ function prints all integers of a list """
    for i in range(0, len(my_list)):
        print("{:d}".format(my_list[i]))
