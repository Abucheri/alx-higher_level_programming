# 0x04. Python - More Data Structures: Set, Dictionary

0. Squared simple
	- Write a function that computes the square value of all integers of a matrix.
		- Prototype: `def square_matrix_simple(matrix=[]):`
		- `matrix` is a 2 dimensional array
		- Returns a new matrix:
			- Same size as `matrix`
			- Each value should be the square of the value of the input
		- Initial matrix should not be modified
		- You are not allowed to import any module
		- You are allowed to use regular `loops`, `map`, etc.
	```
	guillaume@ubuntu:~/0x04$ cat 0-main.py
	#!/usr/bin/python3
	square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

	matrix = [
    		[1, 2, 3],
    		[4, 5, 6],
    		[7, 8, 9]
	]

	new_matrix = square_matrix_simple(matrix)
	print(new_matrix)
	print(matrix)

	guillaume@ubuntu:~/0x04$ ./0-main.py
	[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
	[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	guillaume@ubuntu:~/0x04$ 
	```

1. Search and replace
	- Write a function that replaces all occurrences of an element by another in a new list.
		- Prototype: `def search_replace(my_list, search, replace):`
		- `my_list` is the initial list
		- `search` is the element to replace in the list
		- `replace` is the new element
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x04$ cat 1-main.py
	#!/usr/bin/python3
	search_replace = __import__('1-search_replace').search_replace

	my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
	new_list = search_replace(my_list, 2, 89)

	print(new_list)
	print(my_list)

	guillaume@ubuntu:~/0x04$ ./1-main.py
	[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
	[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
	guillaume@ubuntu:~/0x04$ 
	```

2. Unique addition
	- Write a function that adds all unique integers in a list (only once for each integer).
		- Prototype: `def uniq_add(my_list=[]):`
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x04$ cat 2-main.py
	#!/usr/bin/python3
	uniq_add = __import__('2-uniq_add').uniq_add

	my_list = [1, 2, 3, 1, 4, 2, 5]
	result = uniq_add(my_list)
	print("Result: {:d}".format(result))

	guillaume@ubuntu:~/0x04$ ./2-main.py
	Result: 15
	guillaume@ubuntu:~/0x04$ 
	```

3. Present in both
	- Write a function that returns a set of common elements in two sets.
		- Prototype: `def common_elements(set_1, set_2):`
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x04$ cat 3-main.py
	#!/usr/bin/python3
	common_elements = __import__('3-common_elements').common_elements

	set_1 = { "Python", "C", "Javascript" }
	set_2 = { "Bash", "C", "Ruby", "Perl" }
	c_set = common_elements(set_1, set_2)
	print(sorted(list(c_set)))

	guillaume@ubuntu:~/0x04$ ./3-main.py
	['C']
	guillaume@ubuntu:~/0x04$ 
	```

4. Only differents
	- Write a function that returns a set of all elements present in only one set.
		- Prototype: `def only_diff_elements(set_1, set_2):`
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x04$ cat 4-main.py
	#!/usr/bin/python3
	only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

	set_1 = { "Python", "C", "Javascript" }
	set_2 = { "Bash", "C", "Ruby", "Perl" }
	od_set = only_diff_elements(set_1, set_2)
	print(sorted(list(od_set)))

	guillaume@ubuntu:~/0x04$ ./4-main.py
	['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
	guillaume@ubuntu:~/0x04$ 
	```

5. Number of keys
	- Write a function that returns the number of keys in a dictionary.
		- Prototype: `def number_keys(a_dictionary):`
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x04$ cat 5-main.py
	#!/usr/bin/python3
	number_keys = __import__('5-number_keys').number_keys

	a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
	nb_keys = number_keys(a_dictionary)
	print("Number of keys: {:d}".format(nb_keys))

	guillaume@ubuntu:~/0x04$ ./5-main.py
	Number of keys: 3
	guillaume@ubuntu:~/0x04$ 
	```
