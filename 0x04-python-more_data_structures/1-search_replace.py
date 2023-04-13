#!/usr/bin/python3

def search_replace(my_list, search, replace):

    """ This function replaces all occurrences of an element by another
    in a new list.
    """
    try:
        i = 0
        new_list = [x for x in my_list]
        while i < len(new_list):
            if new_list[i] == search:
                new_list[i] = replace
            i += 1
        return new_list
    except TypeError:
        print("Type missmatch")
