#!/usr/bin/python3

def lookup(obj):
    try:
        return dir(obj)
    except Error as e:
        print(e)
