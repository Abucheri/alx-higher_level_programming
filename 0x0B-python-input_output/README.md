# 0x0B. Python - Input/Output

0. Read file
	- Write a function that reads a text file (`UTF8`) and prints it to stdout:
		- Prototype: `def read_file(filename=""):`
		- You must use the `with` statement
		- You don’t need to manage `file permission` or `file doesn't exist` exceptions.
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x0B$ cat 0-main.py
	#!/usr/bin/python3
	read_file = __import__('0-read_file').read_file

	read_file("my_file_0.txt")

	guillaume@ubuntu:~/0x0B$ cat my_file_0.txt
	We offer a truly innovative approach to education:
	focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

	A school every software engineer would have dreamt of!
	guillaume@ubuntu:~/0x0B$ ./0-main.py
	We offer a truly innovative approach to education:
	focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

	A school every software engineer would have dreamt of!
	guillaume@ubuntu:~/0x0B$ 
	```
	- ___No test cases needed___

1. Write to a file
	- Write a function that writes a string to a text file (`UTF8`) and returns the number of characters written:
		- Prototype: `def write_file(filename="", text=""):`
		- You must use the `with` statement
		- You don’t need to manage file permission exceptions.
		- Your function should create the file if doesn’t exist.
		- Your function should overwrite the content of the file if it already exists.
		- You are not allowed to import any module
	```
	guillaume@ubuntu:~/0x0B$ cat 1-main.py
	#!/usr/bin/python3
	write_file = __import__('1-write_file').write_file

	nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
	print(nb_characters)

	guillaume@ubuntu:~/0x0B$ ./1-main.py
	29
	guillaume@ubuntu:~/0x0B$ cat my_first_file.txt
	This School is so cool!
	guillaume@ubuntu:~/0x0B$ 
	```
	- ___No test cases needed___
