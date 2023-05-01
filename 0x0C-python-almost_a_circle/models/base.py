#!/usr/bin/python3/

"""base module"""


class Base:
    """Base class
    Attributes:
    __nb_objects (int): Keeps track of base objects count
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Base constructor
        Args:
            id (int): The id of Base object
        """
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
