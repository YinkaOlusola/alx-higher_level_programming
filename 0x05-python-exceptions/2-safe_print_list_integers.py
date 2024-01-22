#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the firs x elemets of a list

    args:
            my_list: The list whose elements are to be printed

            x: The numbe of elements to print from the list

            Return: Number of integers printed.

    """
    return_value = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            return_value += 1
        except (ValueError, TypeError, IndexError):
            continue
    print("")
    return (return_value)
