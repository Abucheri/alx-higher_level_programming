#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total = 0
    tWeight = 0
    for score, weight in my_list:
        total += score * weight
        tWeight += weight
    if tWeight == 0:
        return 0
    return total / tWeight
