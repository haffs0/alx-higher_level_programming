#!/usr/bin/python3
"""
This 10-student module has one class Student
"""


class Student:
    """initialized data"""
    def __init__(self, first_name, last_name, age):
        """public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json"""
        dic = {}
        if attrs is not None:
            for item in attrs:
                if item in dir(self):
                    value = getattr(self, item, None)
                    dic[item] = value
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        """reload from json"""
        if (json):
            self.__dict__ = json
