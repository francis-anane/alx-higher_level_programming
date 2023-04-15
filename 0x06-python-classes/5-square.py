#!/usr/bin/python3
""" 5-square module for square operations """


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

    @property
    def size(self):
        """ Gets the value of size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the value of size """
        if not type(value) == int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Prints the square """

        if self.__size == 0:
            print()
        else:
            i = self.__size
            while i > 0:
                print("#" * self.__size)
                i -= 1
