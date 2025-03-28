#!/usr/bin/python3
""" print a dictionary by ordered keys """


def print_sorted_dictionary(a_dictionary):
    dictkeys = list(a_dictionary.keys())
    dictkeys.sort()
    sorted_dict = {i: a_dictionary[i] for i in dictkeys}
    for i, v in sorted_dict.items():
        print("{}: {}".format(i, v))
