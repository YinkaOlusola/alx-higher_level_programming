#!/bin/usr/python3

def safe_print_division(a, b):
    """Divides 2 integers and prints the results

    args:
            a: Dividend - number to be divided
            b: Divisor - number to divide the other

            Return: The result of the division.

    """
    result = 0
    try:
        result = a/b
    except (ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
