#!/usr/bin/env python3
def no_c(my_string):
    newStr = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            newStr += c
    return newStr
