#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Print info abt a Python list
 *
 * @p: pointer to a PyObject representing the list
 *
 * Return: Nothing
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t len, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Python list info\n  [ERROR] Invalid List Object\n");
		return;
	}
	len = PyList_Size(p);
	printf("[*] Python list info\n[*] Size of the Python List =
			%ld\n[*] Allocated = %ld\n", len, ((PyListObject *)p)->allocated);
	for (i = 0; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - print info abt a Python bytes object
 *
 * @p: pointer to a PyObject representing the bytes object
 *
 * Return: Nothing
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t len, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
		return;
	}
	len = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("[.] bytes object info\n  size: %ld\n", len);
	printf("  trying string: %s\n", str);
	printf("  first 10 bytes: ");
	for (i = 0; i < len && i < 10; i++)
	{
		printf("%02x", str[i] & 0xFF);
		if (i < 9)
			printf(" ");
	}
	printf(" ");
}
