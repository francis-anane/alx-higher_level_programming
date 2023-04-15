#!/usr/bin/python3

""" 1-rectangle module for rectangle operations """


class Rectangle:
    """ This class defines a rectangle """

    def __init__(self, width=0, hight=0):
        """ The class initializer.
        Args:
            width (int): The width of the rectangle, (defaults to 0).
            hight (int): The hight of the rectangle, (defaults to 0).

        Raises:
            TypeError: If width or hight is not an integer.
            ValueError: If width or hight is less than zero.
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(hight) != int:
            raise TypeError("hight must be an integer")
        elif hight < 0:
            raise ValueError("hight must be >= 0")
        else:
            self.__hight = hight

    @property
    def width(self):
        """ Gets the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the value of width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def hight(self):
        """ Gets the hight value """

        return self.__hight

    @hight.setter
    def hight(self, value):
        """ Sets the hight value """

        if type(value) != int:
            raise TypeError("hight must be an integer")
        elif value < 0:
            raise ValueError("hight must be >= 0")
        else:
            self.__hight = value
