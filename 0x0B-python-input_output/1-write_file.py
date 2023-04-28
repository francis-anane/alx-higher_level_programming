#!/usr/bin/python3

"""1-write_file module to write to a file"""


def write_file(filename="", text=""):
    """Write text to a file
    Args:
        filename (str): the filename
        text (str): The text to write
    Return: Number of characters written
    """

    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
