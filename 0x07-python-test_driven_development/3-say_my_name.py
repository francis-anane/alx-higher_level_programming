#!/usr/bin/python3

""" 3-say_my_name module for printing a name.
"""


def say_my_name(first_name, last_name=" "):
    """ Prints out a name

    Args:
        first_name (str): the first name
        last_name (str): the last name, (defaults to " ")
    Raises:
          TypeError: If first_name or last_name is not a string.
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        if last_name != " ":
            print(f"My name is {first_name} {last_name}")
        else:
            print(f"My name is {first_name}{last_name}")
