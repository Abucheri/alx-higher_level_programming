#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    adds = add(a, b)
    subs = sub(a, b)
    muls = mul(a, b)
    divs = div(a, b)
    print("{} + {} = {}".format(a, b, adds))
    print("{} - {} = {}".format(a, b, subs))
    print("{} * {} = {}".format(a, b, muls))
    print("{} / {} = {}".format(a, b, divs))
