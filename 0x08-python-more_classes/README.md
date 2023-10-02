# 0x08. Python - More Classes and Objects

0. Simple rectangle
	- Write an empty class `Rectangle` that defines a rectangle:
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x08$ cat 0-main.py
	#!/usr/bin/python3
	Rectangle = __import__('0-rectangle').Rectangle

	my_rectangle = Rectangle()
	print(type(my_rectangle))
	print(my_rectangle.__dict__)

	guillaume@ubuntu:~/0x08$ ./0-main.py
	<class '0-rectangle.Rectangle'>
	{}
	guillaume@ubuntu:~/0x08$ 
	```

1. Real definition of a rectangle
	- Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)
		- Private instance attribute: `width`:
			- property `def width(self):` to retrieve it
			- property setter `def width(self, value):` to set it:
				- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
				- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
		- Private instance attribute: `height`:
			- property `def height(self):` to retrieve it
			- property setter `def height(self, value):` to set it:
				- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
				- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
		- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x08$ cat 1-main.py
	#!/usr/bin/python3
	Rectangle = __import__('1-rectangle').Rectangle

	my_rectangle = Rectangle(2, 4)
	print(my_rectangle.__dict__)

	my_rectangle.width = 10
	my_rectangle.height = 3
	print(my_rectangle.__dict__)

	guillaume@ubuntu:~/0x08$ ./1-main.py
	{'_Rectangle__height': 4, '_Rectangle__width': 2}
	{'_Rectangle__height': 3, '_Rectangle__width': 10}
	guillaume@ubuntu:~/0x08$ 
	```
	- ___No test cases needed___

2. Area and Perimeter
	- Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)
		- Private instance attribute: `width`:
			- property `def width(self):` to retrieve it
			- property setter `def width(self, value):` to set it:
				- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
				- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
		- Private instance attribute: `height`:
			- property `def height(self):` to retrieve it
			- property setter `def height(self, value):` to set it:
				- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
				- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
		- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
		- Public instance method: `def area(self):` that returns the rectangle area
		- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
			- if `width` or `height` is equal to `0`, perimeter is equal to `0`
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x08$ cat 2-main.py
	#!/usr/bin/python3
	Rectangle = __import__('2-rectangle').Rectangle

	my_rectangle = Rectangle(2, 4)
	print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

	print("--")

	my_rectangle.width = 10
	my_rectangle.height = 3
	print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

	guillaume@ubuntu:~/0x08$ ./2-main.py
	Area: 8 - Perimeter: 12
	--
	Area: 30 - Perimeter: 26
	guillaume@ubuntu:~/0x08$ 
	```
	- ___No test cases needed___

3. String representation
	- Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)
		- Private instance attribute: `width`:
			- property `def width(self):` to retrieve it
			- property setter `def width(self, value):` to set it:
				- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
				- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
		- Private instance attribute: `height`:
			- property `def height(self):` to retrieve it
			- property setter `def height(self, value):` to set it:
				- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
				- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
		- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
		- Public instance method: `def area(self):` that returns the rectangle area
		- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
			- if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
		- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
			- if `width` or `height` is equal to `0`, return an empty string
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x08$ cat 3-main.py
	#!/usr/bin/python3
	Rectangle = __import__('3-rectangle').Rectangle

	my_rectangle = Rectangle(2, 4)
	print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

	print(str(my_rectangle))
	print(repr(my_rectangle))

	print("--")

	my_rectangle.width = 10
	my_rectangle.height = 3
	print(my_rectangle)
	print(repr(my_rectangle))

	guillaume@ubuntu:~/0x08$ ./3-main.py
	Area: 8 - Perimeter: 12
	##
	##
	##
	##
	<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
	--
	##########
	##########
	##########
	<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
	guillaume@ubuntu:~/0x08$ 
	```
	- ___Object address can be different___
	- ___No test cases needed___

4. Eval is magic
	- Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)
		- Private instance attribute: `width`:
			- property `def width(self):` to retrieve it
			- property setter `def width(self, value):` to set it:
				- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
				- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
		- Private instance attribute: `height`:
			- property `def height(self):` to retrieve it
			- property setter `def height(self, value):` to set it:
				- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
				- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
		- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
		- Public instance method: `def area(self):` that returns the rectangle area
		- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
			- if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
		- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
			- if `width` or `height` is equal to `0`, return an empty string
		- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x08$ cat 4-main.py
	#!/usr/bin/python3
	Rectangle = __import__('4-rectangle').Rectangle

	my_rectangle = Rectangle(2, 4)
	print(str(my_rectangle))
	print("--")
	print(my_rectangle)
	print("--")
	print(repr(my_rectangle))
	print("--")
	print(hex(id(my_rectangle)))
	print("--")

	# create new instance based on representation
	new_rectangle = eval(repr(my_rectangle))
	print(str(new_rectangle))
	print("--")
	print(new_rectangle)
	print("--")
	print(repr(new_rectangle))
	print("--")
	print(hex(id(new_rectangle)))
	print("--")

	print(new_rectangle is my_rectangle)
	print(type(new_rectangle) is type(my_rectangle))

	guillaume@ubuntu:~/0x08$ ./4-main.py
	##
	##
	##
	##
	--
	##
	##
	##
	##
	--
	Rectangle(2, 4)
	--
	0x7f09ebf7cc88
	--
	##
	##
	##
	##
	--
	##
	##
	##
	##
	--
	Rectangle(2, 4)
	--
	0x7f09ebf7ccc0
	--
	False
	True
	guillaume@ubuntu:~/0x08$ 
	```
	- ___No test cases needed___

5. Detect instance deletion
	- Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)
		- Private instance attribute: `width`:
			- property `def width(self):` to retrieve it
			- property setter `def width(self, value):` to set it:
				- `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
				- if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
		- Private instance attribute: `height`:
			- property `def height(self):` to retrieve it
			- property setter `def height(self, value):` to set it:
				- `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
				- if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
		- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
		- Public instance method: `def area(self):` that returns the rectangle area
		- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
			- if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
		- `print()` and `str()` should print the rectangle with the character `#`:
			- if `width` or `height` is equal to `0`, return an empty string
		- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
		- Print the message `Bye rectangle`... (... being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x08$ cat 5-main.py
	#!/usr/bin/python3
	Rectangle = __import__('5-rectangle').Rectangle

	my_rectangle = Rectangle(2, 4)
	print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

	del my_rectangle

	try:
    		print(my_rectangle)
	except Exception as e:
    		print("[{}] {}".format(e.__class__.__name__, e))

	guillaume@ubuntu:~/0x08$ ./5-main.py
	Area: 8 - Perimeter: 12
	Bye rectangle...
	[NameError] name 'my_rectangle' is not defined
	guillaume@ubuntu:~/0x08$ ~
	```
	- ___No test cases needed___
