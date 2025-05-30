#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        return None
    finally:
        print("{}".format(result))
