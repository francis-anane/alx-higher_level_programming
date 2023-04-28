#!/usr/bin/python3

"""9-student module to define a student """


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

    def to_json(self):
        """ Returns dictionary object representation of Student"""

        return Student(self.first_name, self.last_name, self.age).__dict__
