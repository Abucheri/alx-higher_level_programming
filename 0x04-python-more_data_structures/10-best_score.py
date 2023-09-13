#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        bScore = max(a_dictionary.values())
        for key, val in a_dictionary.items():
            if val == bScore:
                return key
    return None
