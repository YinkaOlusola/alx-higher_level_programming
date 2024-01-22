#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element

    args:
            my_list_1: First list
            my_list_2: Second list
            list_length: Length of the list to be returned

            Return: A new list of length list_length
    """
    result_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i]/my_list_2[i]
        except (TypeError):
            result = 0
            print("wrong type")
        except (ZeroDivisionError):
            result = 0
            print(division by 0)
        except (IndexError):
            print("out of range")
            result = 0
        finally:
            result_list.append(result)
    return (result_list)
            
