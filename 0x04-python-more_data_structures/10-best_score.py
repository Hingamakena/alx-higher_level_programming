#!/usr/bin/python3

def best_score(a_dictionary):
    for i, j in a_dictionary.items():
        if j is None:
            return None
        return max(a_dictionary[i])
