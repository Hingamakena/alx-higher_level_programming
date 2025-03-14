#!/usr/bin/python3

""" class list inherits from list """
class MyList(list):
    """print the list, but sorted"""

    def print_sorted(self):
        return self.sort()
