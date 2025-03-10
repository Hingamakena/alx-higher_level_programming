#!/usr/bin/python3

if __name__ == "__main__":
    import sys

var = len(sys.argv)

if var == 1:
    print("0 arguments.")
elif var > 1:
    print("{} arguments:".format(var))
    for i in range(1, var):
        print("{}: {}".format(i, sys.argv[i]))
