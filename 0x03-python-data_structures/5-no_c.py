#!/usr/bin/python3

def no_c(my_string):
    """ This function removes the characters c or C from a string """

    mod_str = my_string.translate({ord("c"): None, ord("C"): None})
    return mod_str
