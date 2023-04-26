#!/usr/bin/python3

""" 8-rectangle module
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
