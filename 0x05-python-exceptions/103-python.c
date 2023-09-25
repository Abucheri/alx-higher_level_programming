#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Print information about a Python list object
 *
 * @p: The Python object to inspect
 *
 * Return: Nothing
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyListObject *list;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}
	list = (PyListObject *)p;
	size = PyList_GET_SIZE(p);
	printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*]
			Allocated = %ld\n", size, list->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Print information about a Python bytes object
 *
 * @p: The Python object to inspect
 *
 * Return: Nothing
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	PyBytesObject *bytes;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}
	bytes = (PyBytesObject *)p;
	size = PyBytes_GET_SIZE(p);
	printf("[.] bytes object info\n  size: %ld\n", size);
	printf("  trying string: %s\n", PyBytes_AsString(p));
	printf("  first %ld bytes: ", (size > 10) ? 10 : size);
	for (i = 0; i < 10 && i < size; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AS_STRING(p)[i]);
		if (i < 9 && i < size - 1)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_float - Print information about a Python float object
 *
 * @p: The Python object to inspect
 *
 * Return: Nothing
 */

void print_python_float(PyObject *p)
{
	PyObject *str_repr;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}
	str_repr = PyObject_Repr(p);
	printf("[.] float object info\n  value: %s\n", PyUnicode_AsUTF8(str_repr));
	Py_DECREF(str_repr);
}
