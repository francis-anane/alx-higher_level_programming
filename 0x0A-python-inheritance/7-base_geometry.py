#!/usr/bin/python3

""" 7-base_geometry module
"""


class BaseGeometry:
    """ Geometry class """

    def area(self):
        """ raises an exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value

        Args:
            name (str): The name string
            value (int): The value
            Raises:
                  TypeError: If value is not an integer
                  ValueError: If value is less than or equal to 0

        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
