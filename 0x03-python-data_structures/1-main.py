#!/usr/bin/python3

""" import function from function name im file """
element_at = __import__('1-element_at').element_at

mylist = [1,2,3,4,5]

idx = 9
print("element at index {} is {}".format(idx, element_at(mylist, idx)))
