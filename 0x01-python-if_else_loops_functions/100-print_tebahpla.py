#!/usr/bin/python3
a = 0
for alph in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(alph - a)), end='')
    a = 32 if a == 0 else 0
