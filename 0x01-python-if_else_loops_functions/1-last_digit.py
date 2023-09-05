#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_digit = abs(number) % 10
if number < 0:
    l_digit = -l_digit
if l_digit > 5:
    msg = "greater than 5"
elif l_digit == 0:
    msg = "0"
else:
    msg = "less than 6 and not 0"
print(f"Last digit of {number} is {l_digit} and is {msg}")
