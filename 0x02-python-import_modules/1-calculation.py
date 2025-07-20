#!/usr/bin/python3

""" import multiple functions from a single file """

from calculator_1 import add, sub, mul, div

""" defining variables """
a = 10
b = 5

""" printing in format to functions """

print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
