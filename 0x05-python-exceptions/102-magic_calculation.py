#!/usr/bin/python3
"""Module defines magic_calculation"""


def magic_calculation(a, b):
    """Imitates the behaviour of a give byte code """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
