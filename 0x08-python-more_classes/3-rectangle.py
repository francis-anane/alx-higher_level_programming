#!/usr/bin/python3

""" 3-rectangle module for rectangle operations """


class Rectangle:
    """ This class defines a rectangle """

    def __init__(self, width=0, height=0):
        """ The class initializer.
        Args:
            width (int): The width of the rectangle, (defaults to 0).
            height (int): The height of the rectangle, (defaults to 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than zero.
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

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
    def height(self):
        """ Gets the height value """

        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height value """

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ Returns the area of the rectangle."""

        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of the rectangle."""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Returns the rectangle in a print form. """

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rect = ""
            h = self.__height
            while h > 0:
                rect += ("#" * self.__width)
                h -= 1
                if h != 0:
                    rect += "\n"
            return rect
