#!/usr/bin/env python3
def no_c(my_string):
    newStr = [c for c in my_string if c != 'c' and c != 'C']
    return "".join(newStr)
