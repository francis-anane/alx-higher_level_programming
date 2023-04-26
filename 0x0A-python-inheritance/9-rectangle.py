#!/usr/bin/python3

""" 9-rectangle module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Initialize Rectangle

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle

        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Return area of Rectangle """

        return self.__width * self.__height

    def __str__(self):
        """ Return string representation of Rectangle """

        return f"[Rectangle] {self.__width}/{self.__height}"
