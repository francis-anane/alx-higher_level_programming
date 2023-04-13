#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ This function prints x elements of a list. """

    try:
        i = 0
        while x > 0:
            print("{}".format(my_list[i]), end='')
            x = x - 1
            i = i + 1
        print()

    except IndexError:
        print()
    finally:
        return i
