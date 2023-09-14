#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dKey = [key for key, val in a_dictionary.items() if val == value]
    for key in dKey:
        del a_dictionary[key]
    return a_dictionary
