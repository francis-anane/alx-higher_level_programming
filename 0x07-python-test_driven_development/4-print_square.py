#!/usr/bin/python3

""" 4-print_square module for printing a square.
"""


def print_square(size):
    """ Prints a square

    Args:
        size (int): The size length of the square
    Raises:
         TypeError: If size is not an integer or size is a float less than 0
         ValueError: If size is an integer less than 0
    """

    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")
    elif type(size) == float and int(size) < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        return
    else:
        size = int(size)
        i = size
        while i > 0:
            print("#" * size)
            i -= 1
