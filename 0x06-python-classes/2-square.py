#!/usr/bin/python3
""" 2-square module for square operations """


class Square:
    """ This class defines a square """
    def __init__(self, size=0):
        """ The class initializer.
        Args:
        size (int): The size of the squre, (defaults to 0).
        """

        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
