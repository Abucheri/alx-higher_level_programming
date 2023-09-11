#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        fChar = None
    else:
        fChar = sentence[0]
    return len(sentence), fChar
