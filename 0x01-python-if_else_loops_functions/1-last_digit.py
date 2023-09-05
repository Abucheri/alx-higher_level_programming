#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = abs(number) % 10
if l_digit > 5:
    msg = "and is greater than 5"
elif l_digit == 0:
    msg = "and is 0"
else:
    msg = "and is less than 6 and not 0"
output = "Last digit of {} is {} {}".format(number, l_digit, msg)
print(output)
