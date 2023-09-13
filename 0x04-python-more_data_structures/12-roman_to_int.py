#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    romDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    res = 0
    pval = 0
    for char in roman_string[::-1]:
        val = romDict.get(char)
        if val is None:
            return 0
        if val >= pval:
            res += val
        else:
            res -= val
        pval = val
        return res
