#!/usr/bin/python3

def uniq_add(my_list=[]):

    """ This function adds all unique integers in a list
    (only once for each integer).
    """
    try:
        result = 0
        data = set(my_list)
        for i in data:
            result += i
        return result
    except TypeError:
        print("Argument parsed is not an integer list")
