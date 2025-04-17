#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        for i in range(0, my_list[x]):
            print("{:d}".format(my_list[i]))
    except TypeError as e:
        print("string format not supported")
