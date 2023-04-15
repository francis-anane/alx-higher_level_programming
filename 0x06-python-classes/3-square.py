#!/usr/bin/python3
""" 3-square module for square operations """


class Square:
    """ This class defines a square """
    def __init__(self, size=0):
        """ The class initializer.
        Args:
        size (int): The size of the squre, (defaults to 0).
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than zero
        """
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Returns the area of the square."""
        return self.__size**2
