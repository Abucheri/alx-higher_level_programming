#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            upperC = chr(ord(char) - ord('a') + ord('A'))
            result += upperC
        else:
            result += char
    print("{}".format(result))
