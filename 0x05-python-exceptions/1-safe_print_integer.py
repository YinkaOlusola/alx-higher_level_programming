#!/usr/bin/python3

def safe_print_integer(value):
    """Prints x elements of a list

    args:
            value: Integer to be printed

            Return: True or False

    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

    print("\n")
