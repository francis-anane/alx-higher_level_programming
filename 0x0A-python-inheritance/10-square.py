#!/usr/bin/python3

""" 10-square module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size):
        """ Initialize Square

        Args:
            size (int): The size of the square

        """

        self.integer_validator("size", size)
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """ Return area of the Square """
        return self.__size**2
