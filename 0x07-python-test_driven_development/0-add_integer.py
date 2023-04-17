#!/usr/bin/python3

""" 0-add_integer module for addition.
"""


def add_integer(a, b=98):
    """ Adds two integers

    Args:
        a (int): the first operand
        b (int): the second operand, (defaults to 98)
    Raises:
          TypeError: If a or b is not an integer or float.
    Returns:
        int: Value of the addition.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
