#!/usr/bin/python3
""" 6-square module for square operations """


class Square:
    """ This class defines a square """
    def __init__(self, size=0, position=(0, 0)):
        """ The class initializer.
        Args:
            size (int): The size of the squre, (defaults to 0).
            position (tuple): The position of the sqaure.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero
            TypeError: If position is not a tuple with two integer values
        greater than zero.
an integer.
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if (type(position) != tuple) or (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(position[0]) != int) or (type(position[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not position[0] >= 0) or (not position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
        if type(value) != int:
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
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            while i > 0:
                print(" " * self.__position[0] + "#" * self.__size)
                i -= 1

    @property
    def position(self):
        """ Get the position value """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position value """
        if (type(value) != tuple) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) != int) or (type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (not value[0] >= 0) and (not value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
