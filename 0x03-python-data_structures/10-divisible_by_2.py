#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    """ This function finds all multiples of 2 in a list.
    """


    llen = len(my_list)
    if llen == 0:
        return (None)
    else:
        isdivisble = []
        for i in my_list:
            if i % 2 == 0:
                isdivisble.append(True)
            else:
                isdivisble.append(False)
        return (isdivisble)
