#!/usr/bin/python3
def uniq_add(my_list=[]):
    uList = []
    res = 0
    for num in my_list:
        if num not in uList:
            uList.append(num)
            res += num
    return res
