#!/usr/bin/python3
""" class square defining a square"""


class Square:
    """private instance size
        size must be an integer"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
