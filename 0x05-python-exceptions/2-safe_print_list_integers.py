#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ This function prints the first x elements of a list and
    only integers.
    """

    i = 0
    count = 0
    while x > 0:
        try:
            print("{:d}".format(my_list[i]), end='')
            count = count + 1
            x = x - 1
            i = i + 1
        except (ValueError, TypeError):
            x = x - 1
            i = i + 1
    print()
    return count
