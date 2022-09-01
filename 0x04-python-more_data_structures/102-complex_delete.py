#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dict = [(k, v) for k, v in a_dictionary.items()]
    for k, v in a_dict:
        if v is value:
            del a_dictionary[k]
    return a_dictionary
