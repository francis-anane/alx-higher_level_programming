#!/usr/bin/python3

"""0-read_file module to read a file"""


def read_file(filename=""):
    """Read and print a text file to stdout
    Args:
        filename (str): the filename
    """

    with open(filename, "r", encoding="utf-8") as a_file:
        print(a_file.read(), end="")
