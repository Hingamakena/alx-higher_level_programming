#!/usr/bin/python3
""" print a dictionary by ordered keys """


def print_sorted_dictionary(a_dictionary):
    sorted_dict = {i: a_dictionary[i] for i in sorted(a_dictionary)}
    for i, v in sorted_dict.items():
        print("{}: {}".format(i, v))
