#!/usr/bin/python3

""" functin that returns a set of common elements """
def common_elements(set_1, set_2):
    for i in range(0, len(set_1)):
        for j in range(0, len(set_2)):
            if set_1[i] == set_2[j]:
                return i
    return j
