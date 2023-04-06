#!/usr/bin/python3

def max_integer(my_list=[]):

    """ This function finds the biggest integer of a list.
    """

    llen = len(my_list)
    if llen == 0:
        return (None)
    else:
        max_int = my_list[0]
        for i in my_list:
            if i > max_int:
                max_int = i
        return (max_int)
