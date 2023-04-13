#!/usr/bin/python3
def safe_print_division(a, b):
    """ This function divides 2 integers and prints the result.
    """

    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result))
        return result
