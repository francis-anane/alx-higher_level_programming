#!/usr/bin/python3

"""11-student module to define a student """


class Student:
    """ A student class """

    def __init__(self, first_name, last_name, age):
        """ Initialize student
    Args:
        first_name: The student's first name
        last_name: The student's last name
        age: The student's age
    """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns dictionary object representation of Student
        Args:
            attrs: filter for return object
        """
        cls_dict = Student(self.first_name, self.last_name, self.age).__dict__

        if type(attrs) == list:
            data = {}
            [data.update({k: cls_dict[k]}) for k in attrs if k in cls_dict and
             type(k) == str]
            return data
        return cls_dict

    def reload_from_json(self, json):
        """ Replace Student data
        Args:
            json (dict): The data to replace with
        """
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
