#!/usr/bin/python3

"""2-append_write module to append text to a file"""


def append_write(filename="", text=""):
    """Append text to a file
    Args:
        filename (str): the filename
        text (str): The text to append
    Return: Number of characters written
    """

    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
