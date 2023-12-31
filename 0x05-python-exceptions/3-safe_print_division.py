#!/usr/bin/python3
def safe_print_division(a, b):
    dividend = 0

    try:
        dividend = a / b
    except ZeroDivisionError:
        dividend = None
    finally:
        print("Inside result: {}".format(dividend))
        return dividend
