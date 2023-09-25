#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            quotient = 0
            if i < len(my_list_1) and i < len(my_list_2):
                element_1 = my_list_1[i]
                element_2 = my_list_2[i]
                if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                    if element_2 != 0:
                        quotient = element_1 / element_2
                    else:
                        print("division by 0")
                else:
                    print("wrong type")
            else:
                print("out of range")
        except ZeroDivisionError:
            quotient = 0
        finally:
            result.append(quotient)
    return result
