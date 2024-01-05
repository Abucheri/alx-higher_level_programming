#!/usr/bin/python3
"""Find peak in unsorted list of integers"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return (max(list_of_integers[low], list_of_integers[low - 1])
            if low != 0 else list_of_integers[0])
