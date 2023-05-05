#!/usr/bin/python3/

"""base module"""

import json


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
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return json string representation of a list of dictionaries
        Args:
            list_dictionaries (list): A list of dictionaries
        """

        if list_dictionaries is None:
            return "[]"

        if type(list_dictionaries) == list:
            if len(list_dictionaries) == 0:
                return "[]"
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of list_objs to a file
        Args:
            cls: object instance
            list_objs: list of objects to write string represenration of
        """

        if list_objs is None or len(list_objs) == 0:
            with open(cls.__name__ + ".json", "w") as a_file:
                a_file.write("[]")
            return

        try:
            """Create a dictionary to store object_type as keys to a list
            containing json string of object attributes
            """
            obj_names = {}
            for obj in list_objs:
                if type(obj).__name__ not in obj_names.keys():
                    # add key/value to obj_names data
                    obj_names.update({type(obj).__name__: []})
            for obj in list_objs:
                # update obj_names data by appending to the lists
                obj_names[type(obj).__name__].append(obj.to_dictionary())
            # write objects data to file
            for typ in obj_names:
                with open(typ + ".json", "w") as a_file:
                    a_file.write(obj.to_json_string(obj_names[typ]))
        except (NameError, AttributeError, TypeError):
            pass  # pass for now

    @staticmethod
    def from_json_string(json_string):
        """returns a list of JSON string representation
        Args:
            json_string : the json string to get list from
        Return: The list from the string
        """

        if json_string is None:
            return []
        try:
            return list(json.loads(json_string))
        except TypeError:
            pass  # pass for now

    @classmethod
    def create(cls, **dictionary):
        """ Return an instance with all attributes set
        Args:
            cls: object instance
            dictionary: key/word arguments to set instance attribute values
        """
        try:
            instance = cls(10, 10)
            instance.update(**dictionary)
            return instance

        except (TypeError, NameError, AttributeError):
            pass  # pass for now

    @classmethod
    def load_from_file(cls):
        """ Return a list of instances
        Args:
            cls: current class using the method
        """

        try:
            instances = []
            with open(cls.__name__ + ".json", "r") as a_file:
                json_str = a_file.read()
                json_list = cls.from_json_string(json_str)
            for lst in json_list:
                instances.append(cls.create(**lst))
            return instances
        except FileNotFoundError:
            return []
