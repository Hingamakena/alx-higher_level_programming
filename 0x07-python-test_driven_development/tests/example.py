#!/usr/bin/python3
"""
>>add(5, 10)
15
"""
def add(a, b):

    """
    >>> add(9, 0)
    9
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
