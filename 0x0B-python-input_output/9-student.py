#!/usr/bin/python3
"""
This 9-student module has one class Student
"""


class Student:
    """initialized data"""
    def __init__(self, first_name, last_name, age):
        """public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
