#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    args:
            my_list (list): The list to be printed.
            x (int): The number of elements to be printed from my_list.

            Return: The number of elements printed.

    """
    return_ = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            return_ += 1
        except IndexError:
            break
    print("")
    return (return_)
