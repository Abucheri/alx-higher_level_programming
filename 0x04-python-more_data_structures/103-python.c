#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>

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
	PyListObject *list = (PyListObject *)p;
	Py_ssize_t size = PyList_GET_SIZE(p);
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
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
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t size = PyBytes_GET_SIZE(p);
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", PyUnicode_1BYTE_DATA(p));
	printf("  first %ld bytes:", size <= 10 ? size : 10);
	for (i = 0; i < (size <= 10 ? size : 10); i++)
	{
		printf(" %02x", bytes->ob_sval[i]);
	}
	printf("\n");
}
