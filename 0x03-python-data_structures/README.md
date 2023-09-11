# 0x03. Python - Data Structures: Lists, Tuples

0. Print a list of integers
	- Write a function that prints all integers of a list.
		- Prototype: `def print_list_integer(my_list=[]):`
		- Format: one integer per line. See example
		- You are not allowed to import any module
		- You can assume that the list only contains integers
		- You are not allowed to cast integers into strings
		- You have to use `str.format()` to print integers

	```
	guillaume@ubuntu:~/0x03$ cat 0-main.py
	#!/usr/bin/python3
	print_list_integer = __import__('0-print_list_integer').print_list_integer

	my_list = [1, 2, 3, 4, 5]
	print_list_integer(my_list)

	guillaume@ubuntu:~/0x03$ ./0-main.py
	1
	2
	3
	4
	5
	guillaume@ubuntu:~/0x03$ 
	```

1. Secure access to an element in a list
	- Write a function that retrieves an element from a list like in C.
		- Prototype: `def element_at(my_list, idx):`
		- If `idx` is negative, the function should return `None`
		- If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
		- You are not allowed to import any module
		- You are not allowed to use `try/except`

	```
	guillaume@ubuntu:~/0x03$ cat 1-main.py
	#!/usr/bin/python3
	element_at = __import__('1-element_at').element_at

	my_list = [1, 2, 3, 4, 5]
	idx = 3
	print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

	guillaume@ubuntu:~/0x03$ ./1-main.py
	Element at index 3 is 4
	guillaume@ubuntu:~/0x03$ 
	```
