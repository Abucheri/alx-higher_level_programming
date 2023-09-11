#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        a = 0
    else:
        a = tuple_a[0]
    if len(tuple_b) < 2:
        b = 0
    else:
        b = tuple_b[0]
    if len(tuple_a) < 2:
        c = 0
    else:
        c = tuple_a[1]
    if len(tuple_b) < 2:
        d = 0
    else:
        d = tuple_b[1]
    res = (a + b, c + d)
    return res
